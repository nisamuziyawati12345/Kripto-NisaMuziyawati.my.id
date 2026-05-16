from flask import Flask, render_template, request, redirect, url_for, flash
from algorithms.caesar import caesar_encrypt, caesar_decrypt
from algorithms.vigenere import vigenere_encrypt, vigenere_decrypt
from algorithms.affine import affine_encrypt, affine_decrypt
from algorithms.hill import hill_encrypt, hill_decrypt
from algorithms.playfair import playfair_encrypt, playfair_decrypt
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "kriptografi-secret-key"

DATABASE = "history.db"


# =========================================================
# DATABASE
# =========================================================

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            algorithm TEXT,
            action TEXT,
            input_text TEXT,
            result_text TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_history(algorithm, action, input_text, result_text):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history (
            algorithm,
            action,
            input_text,
            result_text,
            created_at
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        algorithm,
        action,
        input_text,
        result_text,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# =========================================================
# HOME
# =========================================================

@app.route('/')
def index():
    history = get_history()

    return render_template(
        'index.html',
        history=history
    )


# =========================================================
# PROCESS ENCRYPT / DECRYPT
# =========================================================

@app.route('/process', methods=['POST'])
def process():

    algorithm = request.form.get('algorithm')
    action = request.form.get('action')
    text = request.form.get('text')

    result = ""
    steps = []
    formula = ""

    try:

        # =================================================
        # VALIDASI INPUT
        # =================================================

        if not text or text.strip() == "":
            flash("Input text tidak boleh kosong!", "danger")
            return redirect(url_for('index'))

        # =================================================
        # CAESAR CIPHER
        # =================================================

        if algorithm == 'caesar':

            shift = request.form.get('shift')

            if shift == "":
                flash("Shift Caesar wajib diisi!", "danger")
                return redirect(url_for('index'))

            shift = int(shift)

            if shift < 1 or shift > 25:
                flash("Shift Caesar harus antara 1 - 25", "danger")
                return redirect(url_for('index'))

            formula = "E(x) = (x + k) mod 26"

            if action == 'encrypt':
                result, steps = caesar_encrypt(text, shift)
            else:
                formula = "D(x) = (x - k) mod 26"
                result, steps = caesar_decrypt(text, shift)

        # =================================================
        # VIGENERE CIPHER
        # =================================================

        elif algorithm == 'vigenere':

            key = request.form.get('key')

            if not key:
                flash("Key Vigenere wajib diisi!", "danger")
                return redirect(url_for('index'))

            formula = "Ci = (Pi + Ki) mod 26"

            if action == 'encrypt':
                result, steps = vigenere_encrypt(text, key)
            else:
                formula = "Pi = (Ci - Ki) mod 26"
                result, steps = vigenere_decrypt(text, key)

        # =================================================
        # AFFINE CIPHER
        # =================================================

        elif algorithm == 'affine':

            a = request.form.get('a')
            b = request.form.get('b')

            if a == "" or b == "":
                flash("Nilai a dan b wajib diisi!", "danger")
                return redirect(url_for('index'))

            a = int(a)
            b = int(b)

            valid_a = [
                1, 3, 5, 7, 9, 11,
                15, 17, 19, 21, 23, 25
            ]

            if a not in valid_a:
                flash(
                    "Nilai a harus relatif prima dengan 26",
                    "danger"
                )
                return redirect(url_for('index'))

            formula = "E(x) = (ax + b) mod 26"

            if action == 'encrypt':
                result, steps = affine_encrypt(text, a, b)
            else:
                formula = "D(x) = a^-1(x - b) mod 26"
                result, steps = affine_decrypt(text, a, b)

        # =================================================
        # HILL CIPHER
        # =================================================

        elif algorithm == 'hill':

            hill_key = request.form.get('hill_key')

            if not hill_key:
                flash("Matrix key Hill Cipher wajib diisi!", "danger")
                return redirect(url_for('index'))

            formula = "C = K × P mod 26"

            if action == 'encrypt':
                result, steps = hill_encrypt(text, hill_key)
            else:
                formula = "P = K^-1 × C mod 26"
                result, steps = hill_decrypt(text, hill_key)

        # =================================================
        # PLAYFAIR CIPHER
        # =================================================

        elif algorithm == 'playfair':

            playfair_key = request.form.get('playfair_key')

            if not playfair_key:
                flash("Key Playfair wajib diisi!", "danger")
                return redirect(url_for('index'))

            formula = "Playfair 5x5 Matrix Encryption"

            if action == 'encrypt':
                result, steps = playfair_encrypt(
                    text,
                    playfair_key
                )
            else:
                formula = "Playfair 5x5 Matrix Decryption"

                result, steps = playfair_decrypt(
                    text,
                    playfair_key
                )

        else:
            flash("Algoritma tidak valid!", "danger")
            return redirect(url_for('index'))

        # =================================================
        # SAVE HISTORY
        # =================================================

        save_history(
            algorithm,
            action,
            text,
            result
        )

        # =================================================
        # RENDER RESULT
        # =================================================

        return render_template(
            'result.html',
            algorithm=algorithm,
            action=action,
            input_text=text,
            result=result,
            steps=steps,
            formula=formula
        )

    except ValueError:
        flash("Input harus berupa angka yang valid!", "danger")
        return redirect(url_for('index'))

    except Exception as e:
        flash(f"Terjadi error: {str(e)}", "danger")
        return redirect(url_for('index'))


# =========================================================
# DELETE HISTORY
# =========================================================

@app.route('/delete-history')
def delete_history():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM history")

    conn.commit()
    conn.close()

    flash("History berhasil dihapus!", "success")

    return redirect(url_for('index'))


# =========================================================
# ABOUT PAGE
# =========================================================

@app.route('/about')
def about():
    return render_template('about.html')


# =========================================================
# ERROR HANDLER
# =========================================================

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# =========================================================
# DELETE SINGLE HISTORY
# =========================================================

@app.route('/delete/<int:id>')
def delete_single_history(id):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM history WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    flash("History berhasil dihapus!", "success")

    return redirect(url_for('index'))

# =========================================================
# MAIN
# =========================================================

import os

if __name__ == '__main__':
    init_db()

    port = int(os.environ.get("PORT", 5000))
    app.run(
        host='0.0.0.0',
        port=port
    )
