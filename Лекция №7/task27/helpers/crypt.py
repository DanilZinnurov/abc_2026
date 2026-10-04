def caesar_cipher(message, filename_cipher):
    ALPHABET_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ALPHABET_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ALPHABET_SIZE = 33
    test_text = ''

    with open(filename_cipher, "w", encoding="utf-8") as f_out:
        for line_num, line in enumerate(message.split()):
            test_text += line
            encrypted_line = ""

            for char in line:
                if char in ALPHABET_UPPER:
                    old_index = ALPHABET_UPPER.index(char)
                    new_index = (old_index - line_num) % ALPHABET_SIZE
                    encrypted_line += ALPHABET_UPPER[new_index]

                elif char in ALPHABET_LOWER:
                    old_index = ALPHABET_LOWER.index(char)
                    new_index = (old_index - line_num) % ALPHABET_SIZE
                    encrypted_line += ALPHABET_LOWER[new_index]

                else:
                    encrypted_line += char

            f_out.write(encrypted_line)

    print("Шифрование завершено! Результат записан в encrypted_message.txt")

    print("\n--- Зашифрованный текст ---")
    with open(filename_cipher, "r", encoding="utf-8") as f:
        return f.read()
