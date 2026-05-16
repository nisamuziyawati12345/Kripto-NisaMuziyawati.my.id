import numpy as np


# =========================================================
# KONVERSI HURUF
# =========================================================

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def char_to_num(char):
    return ord(char.upper()) - ord('A')


def num_to_char(num):
    return chr((num % 26) + ord('A'))


# =========================================================
# PARSE MATRIX KEY
# =========================================================

def parse_key_matrix(key_string):

    rows = key_string.strip().split(',')

    matrix = []

    for row in rows:
        matrix.append(
            [int(x) for x in row.strip().split()]
        )

    matrix = np.array(matrix)

    # VALIDASI
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError(
            "Matrix harus persegi (2x2 atau 3x3)"
        )

    if matrix.shape[0] not in [2, 3]:
        raise ValueError(
            "Hill Cipher hanya support 2x2 atau 3x3"
        )

    return matrix


# =========================================================
# CEK MATRIX INVERTIBLE
# =========================================================

def mod_inverse(a, m):

    a = a % m

    for x in range(1, m):

        if (a * x) % m == 1:
            return x

    return None


def matrix_mod_inverse(matrix, modulus):

    det = int(round(np.linalg.det(matrix)))

    det_mod = det % modulus

    det_inv = mod_inverse(det_mod, modulus)

    if det_inv is None:
        raise ValueError(
            "Determinan matrix tidak memiliki inverse mod 26"
        )

    # ADJOINT MATRIX
    matrix_inv = np.linalg.inv(matrix)

    adjugate = np.round(
        matrix_inv * det
    ).astype(int)

    inverse_matrix = (
        det_inv * adjugate
    ) % modulus

    return inverse_matrix.astype(int)


# =========================================================
# BERSIHKAN TEXT
# =========================================================

def clean_text(text):

    cleaned = ""

    for char in text:

        if char.isalpha():
            cleaned += char.upper()

    return cleaned


# =========================================================
# TAMBAH PADDING
# =========================================================

def add_padding(text, size):

    while len(text) % size != 0:
        text += 'X'

    return text


# =========================================================
# HILL ENCRYPT
# =========================================================

def hill_encrypt(text, key_string):

    matrix = parse_key_matrix(key_string)

    size = matrix.shape[0]

    cleaned_text = clean_text(text)

    cleaned_text = add_padding(
        cleaned_text,
        size
    )

    result = ""

    steps = []

    index = 1

    # PROSES PER BLOK
    for i in range(0, len(cleaned_text), size):

        block = cleaned_text[i:i + size]

        vector = np.array([
            char_to_num(c)
            for c in block
        ])

        # MATRIX MULTIPLICATION
        encrypted_vector = np.dot(
            matrix,
            vector
        ) % 26

        encrypted_block = ''.join(
            num_to_char(num)
            for num in encrypted_vector
        )

        result += encrypted_block

        # DETAIL STEP
        steps.append({

            "index": index,

            "plaintext_char": block,

            "plaintext_value": vector.tolist(),

            "key_char": str(matrix.tolist()),

            "key_value": "-",

            "calculation":
                f"{matrix.tolist()} × "
                f"{vector.tolist()} mod 26 = "
                f"{encrypted_vector.tolist()}",

            "result_char": encrypted_block

        })

        index += 1

    return result, steps


# =========================================================
# HILL DECRYPT
# =========================================================

def hill_decrypt(text, key_string):

    matrix = parse_key_matrix(key_string)

    inverse_matrix = matrix_mod_inverse(
        matrix,
        26
    )

    size = matrix.shape[0]

    cleaned_text = clean_text(text)

    cleaned_text = add_padding(
        cleaned_text,
        size
    )

    result = ""

    steps = []

    index = 1

    # PROSES PER BLOK
    for i in range(0, len(cleaned_text), size):

        block = cleaned_text[i:i + size]

        vector = np.array([
            char_to_num(c)
            for c in block
        ])

        # MATRIX MULTIPLICATION
        decrypted_vector = np.dot(
            inverse_matrix,
            vector
        ) % 26

        decrypted_block = ''.join(
            num_to_char(num)
            for num in decrypted_vector
        )

        result += decrypted_block

        # DETAIL STEP
        steps.append({

            "index": index,

            "ciphertext_char": block,

            "ciphertext_value": vector.tolist(),

            "key_char": str(inverse_matrix.tolist()),

            "key_value": "-",

            "calculation":
                f"{inverse_matrix.tolist()} × "
                f"{vector.tolist()} mod 26 = "
                f"{decrypted_vector.tolist()}",

            "result_char": decrypted_block

        })

        index += 1

    return result, steps