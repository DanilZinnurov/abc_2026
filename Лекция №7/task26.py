#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
#
# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36
#
#
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
#
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!


def load_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    matrix = [[float(num) for num in line.split()] for line in lines]

    lengths = [len(row) for row in matrix]

    if all(length == lengths[0] for length in lengths):
        return matrix
    else:
        return False

result = load_matrix("test_matrix.txt")

if result:
    print("Матрица успешно загружена:")
    for row in result:
        print(row)
else:
    print("Ошибка: строки имеют разную длину")