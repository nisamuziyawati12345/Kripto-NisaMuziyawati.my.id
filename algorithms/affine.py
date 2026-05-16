# =========================================================
# AFFINE CIPHER
# =========================================================

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# =========================================================
# MENCARI MODULAR INVERSE
# =========================================================

def mod_inverse(a, m=26):

    for x in range(1, m):

        if (a * x) % m == 1:
            return x

    return None


# =========================================================
# ENCRYPT
# Formula:
# E(x) = (a*x + b) mod 26
# =========================================================

def affine_encrypt(text, a, b):

    result = ""
    steps = []

    index = 1

    for char in text:

        # =============================================
        # HANYA HURUF
        # =============================================

        if char.isalpha():

            is_upper = char.isupper()

            plain_char = char.upper()

            # Konversi huruf -> angka
            x = ord(plain_char) - ord('A')

            # Rumus affine
            encrypted_value = (a * x + b) % 26

            # Konversi angka -> huruf
            encrypted_char = chr(encrypted_value + ord('A'))

            # Kembalikan lowercase jika awal lowercase
            if not is_upper:
                encrypted_char = encrypted_char.lower()

            result += encrypted_char

            # =============================================
            # SIMPAN STEP
            # =============================================

            steps.append({

                "index": index,

                "plaintext_char": char,
                "plaintext_value": x,

                "key_char": f"a={a}, b={b}",
                "key_value": f"({a},{b})",

                "calculation":
                    f"({a} × {x} + {b}) mod 26 = "
                    f"{encrypted_value}",

                "result_char": encrypted_char

            })

            index += 1

        else:

            # Simpan karakter selain huruf
            result += char

            steps.append({

                "index": index,

                "plaintext_char": char,
                "plaintext_value": "-",

                "key_char": "-",
                "key_value": "-",

                "calculation": "Karakter non-huruf tidak diubah",

                "result_char": char

            })

            index += 1

    return result, steps


# =========================================================
# DECRYPT
# Formula:
# D(x) = a^-1 (x - b) mod 26
# =========================================================

def affine_decrypt(text, a, b):

    result = ""
    steps = []

    index = 1

    # Cari inverse dari a
    a_inverse = mod_inverse(a, 26)

    if a_inverse is None:
        raise ValueError(
            "Nilai a tidak memiliki modular inverse!"
        )

    for char in text:

        # =============================================
        # HANYA HURUF
        # =============================================

        if char.isalpha():

            is_upper = char.isupper()

            cipher_char = char.upper()

            # Huruf -> angka
            y = ord(cipher_char) - ord('A')

            # Rumus decrypt
            decrypted_value = (
                a_inverse * (y - b)
            ) % 26

            # Angka -> huruf
            decrypted_char = chr(
                decrypted_value + ord('A')
            )

            # Kembalikan lowercase
            if not is_upper:
                decrypted_char = decrypted_char.lower()

            result += decrypted_char

            # =============================================
            # SIMPAN STEP
            # =============================================

            steps.append({

                "index": index,

                "ciphertext_char": char,
                "ciphertext_value": y,

                "key_char":
                    f"a⁻¹={a_inverse}, b={b}",

                "key_value":
                    f"({a_inverse},{b})",

                "calculation":
                    f"{a_inverse} × "
                    f"({y} - {b}) mod 26 = "
                    f"{decrypted_value}",

                "result_char": decrypted_char

            })

            index += 1

        else:

            # Simpan karakter non huruf
            result += char

            steps.append({

                "index": index,

                "ciphertext_char": char,
                "ciphertext_value": "-",

                "key_char": "-",
                "key_value": "-",

                "calculation":
                    "Karakter non-huruf tidak diubah",

                "result_char": char

            })

            index += 1

    return result, steps