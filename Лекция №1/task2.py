# todo: Преобразуйте переменную age и foo в число
from openpyxl.pivot.fields import Boolean

age = "23"
foo = "23abc"

age = int(age)
print(age)
# foo = int(foo) ValueError: invalid literal for int() with base 10: '23abc'
# print(foo)

print("=" * 80)

# Преобразуйте переменную age в Boolean
age = "123abc"

age = bool(age)
print(age)

print("=" * 80)

# Преобразуйте переменную flag в Boolean
flag = 1

flag = bool(flag)
print(flag)

print("=" * 80)

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""

print(bool(str_one))
print(bool(str_two))

print("=" * 80)

# Преобразуйте значение 0 и 1 в Boolean

a = 0
b = 1

print(bool(a))
print(bool(b))

print("=" * 80)

# Преобразуйте False в строку

tmp = False
print(str(tmp))
