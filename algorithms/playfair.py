# =========================================================
# PLAYFAIR CIPHER
# =========================================================

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


# =========================================================
# GENERATE 5x5 MATRIX
# =========================================================

def generate_matrix(key):

    key = key.upper().replace("J", "I")

    matrix = []
    used = set()

    # Masukkan key
    for char in key:

        if char.isalpha() and char not in used:

            used.add(char)
            matrix.append(char)

    # Tambahkan alphabet lain
    for char in ALPHABET:

        if char not in used:

            used.add(char)
            matrix.append(char)

    # Ubah jadi matrix 5x5
    matrix_5x5 = []

    for i in range(0, 25, 5):

        matrix_5x5.append(matrix[i:i+5])

    return matrix_5x5


# =========================================================
# FORMAT TEXT
# =========================================================

def prepare_text(text):

    text = text.upper().replace("J", "I")

    clean_text = ""

    for char in text:

        if char.isalpha():

            clean_text += char

    pairs = []

    i = 0

    while i < len(clean_text):

        a = clean_text[i]

        if i + 1 < len(clean_text):

            b = clean_text[i + 1]

            # Huruf sama → tambah X
            if a == b:

                pairs.append(a + "X")
                i += 1

            else:

                pairs.append(a + b)
                i += 2

        else:

            # Tambah X jika ganjil
            pairs.append(a + "X")
            i += 1

    return pairs


# =========================================================
# FIND POSITION
# =========================================================

def find_position(matrix, char):

    for row in range(5):

        for col in range(5):

            if matrix[row][col] == char:

                return row, col


# =========================================================
# ENCRYPT
# =========================================================

def playfair_encrypt(text, key):

    matrix = generate_matrix(key)

    pairs = prepare_text(text)

    result = ""
    steps = []

    index = 1

    for pair in pairs:

        a = pair[0]
        b = pair[1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        # =============================================
        # RULE 1: SAME ROW
        # =============================================

        if row1 == row2:

            c1 = matrix[row1][(col1 + 1) % 5]
            c2 = matrix[row2][(col2 + 1) % 5]

            rule = "Same Row"

        # =============================================
        # RULE 2: SAME COLUMN
        # =============================================

        elif col1 == col2:

            c1 = matrix[(row1 + 1) % 5][col1]
            c2 = matrix[(row2 + 1) % 5][col2]

            rule = "Same Column"

        # =============================================
        # RULE 3: RECTANGLE
        # =============================================

        else:

            c1 = matrix[row1][col2]
            c2 = matrix[row2][col1]

            rule = "Rectangle"

        encrypted_pair = c1 + c2

        result += encrypted_pair

        steps.append({

            "index": index,
            "plaintext_char": pair,
            "ciphertext_char": encrypted_pair,
            "plaintext_value": f"({row1},{col1}) & ({row2},{col2})",
            "ciphertext_value": encrypted_pair,
            "key_char": key,
            "key_value": "5x5 Matrix",
            "calculation": rule,
            "result_char": encrypted_pair,
            "matrix": matrix

        })

        index += 1

    return result, steps


# =========================================================
# DECRYPT
# =========================================================

def playfair_decrypt(text, key):

    matrix = generate_matrix(key)

    pairs = prepare_text(text)

    result = ""
    steps = []

    index = 1

    for pair in pairs:

        a = pair[0]
        b = pair[1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        # =============================================
        # RULE 1: SAME ROW
        # =============================================

        if row1 == row2:

            c1 = matrix[row1][(col1 - 1) % 5]
            c2 = matrix[row2][(col2 - 1) % 5]

            rule = "Same Row"

        # =============================================
        # RULE 2: SAME COLUMN
        # =============================================

        elif col1 == col2:

            c1 = matrix[(row1 - 1) % 5][col1]
            c2 = matrix[(row2 - 1) % 5][col2]

            rule = "Same Column"

        # =============================================
        # RULE 3: RECTANGLE
        # =============================================

        else:

            c1 = matrix[row1][col2]
            c2 = matrix[row2][col1]

            rule = "Rectangle"

        decrypted_pair = c1 + c2

        result += decrypted_pair

        steps.append({

            "index": index,
            "plaintext_char": pair,
            "ciphertext_char": decrypted_pair,
            "plaintext_value": f"({row1},{col1}) & ({row2},{col2})",
            "ciphertext_value": decrypted_pair,
            "key_char": key,
            "key_value": "5x5 Matrix",
            "calculation": rule,
            "result_char": decrypted_pair,
            "matrix": matrix

        })

        index += 1

    return result, steps