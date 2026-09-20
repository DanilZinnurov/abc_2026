# todo: База данных пользователя.
# Задан массив объектов пользователя

# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# #Затем сообщение для ввода
# Ввидите критерии поиска: 16
#
# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

print("Типы сортировки:")
print("1. По возрасту (больше введённого)")
print("2. По первой букве логина")
print("3. По группе")

sort_type = int(input("Введите тип сортировки: "))

if sort_type == 1:
    criterion = int(input("Введите минимальный возраст: "))
    filtered = [u for u in users if u['age'] > criterion]
    filtered.sort(key=lambda u: u['age'])
elif sort_type == 2:
    letter = input("Введите первую букву логина: ").strip().capitalize()
    filtered = [u for u in users if u['login'].startswith(letter)]
    filtered.sort(key=lambda u: u['login'])
elif sort_type == 3:
    group = input("Введите группу: ").strip()
    filtered = [u for u in users if u['group'] == group]
    filtered.sort(key=lambda u: u['group'])
else:
    print("Неверный тип сортировки!")
    filtered = []

for u in filtered:
    print(f"Пользователь: '{u['login']}' возраст {u['age']}, "
          f"группа \"{u['group']}\"")