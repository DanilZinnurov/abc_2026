#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)


def crack_caesar(ciphertext):
    print(f"Зашифрованный текст: {ciphertext}\n")

    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"Сдвиг {shift:2d} (или -{26 - shift:2d}): {decrypted}")

    print("=" * 70)

ciphertext = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
crack_caesar(ciphertext)


# Ответ: Сдвиг 20 (или - 6): although that way may not be obvious at first unless you're dutch