# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

ALPHABET_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ALPHABET_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_SIZE = 33
test_text = ''

with open("message.txt", "r", encoding="utf-8") as f_in, \
     open("encrypted_message.txt", "w", encoding="utf-8") as f_out:
    
    for line_num, line in enumerate(f_in, start=1):
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

print("\n--- Исходный текст ---")
print(test_text)
print("\n--- Зашифрованный текст ---")
with open("encrypted_message.txt", "r", encoding="utf-8") as f:
    print(f.read())
