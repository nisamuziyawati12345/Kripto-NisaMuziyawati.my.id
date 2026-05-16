# =========================================================
# CAESAR CIPHER
# =========================================================

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# =========================================================
# ENCRYPT
# =========================================================

def caesar_encrypt(text, shift):

    result = ""
    steps = []

    for index, char in enumerate(text):

        # =============================================
        # HURUF
        # =============================================

        if char.isalpha():

            is_upper = char.isupper()

            original_char = char

            upper_char = char.upper()

            # KONVERSI HURUF KE ANGKA
            x = ord(upper_char) - ord('A')

            # RUMUS ENKRIPSI
            encrypted_value = (x + shift) % 26

            # KONVERSI KE HURUF
            encrypted_char = chr(encrypted_value + ord('A'))

            # KEMBALIKAN FORMAT ASLI
            if not is_upper:
                encrypted_char = encrypted_char.lower()

            result += encrypted_char

            # STEP DETAIL
            steps.append({

                "plaintext_char": original_char,

                "plaintext_value": x,

                "key_char": shift,

                "key_value": shift,

                "calculation":
                    f"({x} + {shift}) mod 26 = {encrypted_value}",

                "result_char": encrypted_char

            })

        # =============================================
        # SPASI / SIMBOL
        # =============================================

        else:

            result += char

            steps.append({

                "plaintext_char": char,

                "plaintext_value": "-",

                "key_char": "-",

                "key_value": "-",

                "calculation": "Karakter tidak diubah",

                "result_char": char

            })

    return result, steps


# =========================================================
# DECRYPT
# =========================================================

def caesar_decrypt(text, shift):

    result = ""
    steps = []

    for index, char in enumerate(text):

        # =============================================
        # HURUF
        # =============================================

        if char.isalpha():

            is_upper = char.isupper()

            original_char = char

            upper_char = char.upper()

            # KONVERSI HURUF KE ANGKA
            x = ord(upper_char) - ord('A')

            # RUMUS DEKRIPSI
            decrypted_value = (x - shift) % 26

            # KONVERSI KE HURUF
            decrypted_char = chr(decrypted_value + ord('A'))

            # KEMBALIKAN FORMAT ASLI
            if not is_upper:
                decrypted_char = decrypted_char.lower()

            result += decrypted_char

            # STEP DETAIL
            steps.append({

                "ciphertext_char": original_char,

                "ciphertext_value": x,

                "key_char": shift,

                "key_value": shift,

                "calculation":
                    f"({x} - {shift}) mod 26 = {decrypted_value}",

                "result_char": decrypted_char

            })

        # =============================================
        # SPASI / SIMBOL
        # =============================================

        else:

            result += char

            steps.append({

                "ciphertext_char": char,

                "ciphertext_value": "-",

                "key_char": "-",

                "key_value": "-",

                "calculation": "Karakter tidak diubah",

                "result_char": char

            })

    return result, steps