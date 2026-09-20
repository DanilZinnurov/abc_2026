#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]

indices = {}
for i, val in enumerate(mass):
    indices[val] = indices.get(val, []) + [i]

for val, idx_list in indices.items():
    if len(idx_list) < 2:
        print(f"Для числа {val} нет минимального расстояния, т.к. элемент в массиве один.")
        continue

    min_dist = float('inf')
    min_pair = None

    for i in range(len(idx_list) - 1):
        dist = idx_list[i + 1] - idx_list[i]
        if dist < min_dist:
            min_dist = dist
            min_pair = (idx_list[i], idx_list[i + 1])

    print(f"Для числа {val} минимальное расстояние по индексам: "
          f"{min_pair[0]} и {min_pair[1]} (расстояние = {min_dist})")
