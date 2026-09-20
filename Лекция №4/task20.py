#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

with open("inverted_sort.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

lines[-1] += '\n'

with open("inverted_sort.txt", "a", encoding="utf-8") as f:
    f.write('\n\n')
    reversed_lines = lines[::-1]
    print(''.join(reversed_lines))
    f.writelines(reversed_lines)
f.close()