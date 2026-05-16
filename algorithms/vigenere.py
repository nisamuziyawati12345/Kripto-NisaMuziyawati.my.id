# =========================================================
# VIGENERE CIPHER
# =========================================================

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# =========================================================
# MEMBERSIHKAN KEY
# =========================================================

def clean_key(key):

    cleaned = ""

    for char in key:

        if char.isalpha():
            cleaned += char.upper()

    return cleaned


# =========================================================
# ENCRYPT
# =========================================================

def vigenere_encrypt(text, key):

    result = ""
    steps = []

    key = clean_key(key)

    if key == "":
        raise ValueError(
            "Key hanya boleh berisi huruf"
        )

    key_index = 0

    for i, char in enumerate(text):

        # =============================================
        # HANYA HURUF YANG DIENKRIPSI
        # =============================================

        if char.isalpha():

            # Menentukan basis ASCII
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # =============================================
            # PLAINTEXT KE ANGKA
            # =============================================

            plain_value = ord(char.upper()) - ord('A')

            # =============================================
            # KEY CHARACTER
            # =============================================

            current_key = key[
                key_index % len(key)
            ]

            key_value = (
                ord(current_key) - ord('A')
            )

            # =============================================
            # RUMUS VIGENERE
            # Ci = (Pi + Ki) mod 26
            # =============================================

            cipher_value = (
                plain_value + key_value
            ) % 26

            encrypted_char = chr(
                cipher_value + base
            )

            result += encrypted_char

            # =============================================
            # SIMPAN STEP
            # =============================================

            steps.append({

                "index": i + 1,

                "plaintext_char": char,

                "plaintext_value": plain_value,

                "key_char": current_key,

                "key_value": key_value,

                "calculation":
                    f"({plain_value} + "
                    f"{key_value}) mod 26 "
                    f"= {cipher_value}",

                "result_char": encrypted_char

            })

            key_index += 1

        else:

            # =============================================
            # SPASI / TANDA BACA TIDAK DIUBAH
            # =============================================

            result += char

            steps.append({

                "index": i + 1,

                "plaintext_char": char,

                "plaintext_value": "-",

                "key_char": "-",

                "key_value": "-",

                "calculation":
                    "Karakter non-huruf "
                    "tidak dienkripsi",

                "result_char": char

            })

    return result, steps


# =========================================================
# DECRYPT
# =========================================================

def vigenere_decrypt(text, key):

    result = ""
    steps = []

    key = clean_key(key)

    if key == "":
        raise ValueError(
            "Key hanya boleh berisi huruf"
        )

    key_index = 0

    for i, char in enumerate(text):

        # =============================================
        # HANYA HURUF YANG DIDEKRIPSI
        # =============================================

        if char.isalpha():

            # Menentukan basis ASCII
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # =============================================
            # CIPHERTEXT KE ANGKA
            # =============================================

            cipher_value = ord(char.upper()) - ord('A')

            # =============================================
            # KEY CHARACTER
            # =============================================

            current_key = key[
                key_index % len(key)
            ]

            key_value = (
                ord(current_key) - ord('A')
            )

            # =============================================
            # RUMUS VIGENERE
            # Pi = (Ci - Ki) mod 26
            # =============================================

            plain_value = (
                cipher_value - key_value
            ) % 26

            decrypted_char = chr(
                plain_value + base
            )

            result += decrypted_char

            # =============================================
            # SIMPAN STEP
            # =============================================

            steps.append({

                "index": i + 1,

                "ciphertext_char": char,

                "ciphertext_value": cipher_value,

                "key_char": current_key,

                "key_value": key_value,

                "calculation":
                    f"({cipher_value} - "
                    f"{key_value}) mod 26 "
                    f"= {plain_value}",

                "result_char": decrypted_char

            })

            key_index += 1

        else:

            # =============================================
            # SPASI / TANDA BACA TIDAK DIUBAH
            # =============================================

            result += char

            steps.append({

                "index": i + 1,

                "ciphertext_char": char,

                "ciphertext_value": "-",

                "key_char": "-",

                "key_value": "-",

                "calculation":
                    "Karakter non-huruf "
                    "tidak didekripsi",

                "result_char": char

            })

    return result, steps