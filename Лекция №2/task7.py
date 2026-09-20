#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))

AC = abs(A - C)
BC = abs(B - C)

print(AC)
print(BC)
print(AC + BC)
