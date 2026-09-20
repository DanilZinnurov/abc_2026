#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
#              "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
#              "Наивный байесовский классификатор", "CART" ]
#
# # Каждое значение из списка должно находится на отдельной строке.
# # Пример файла algoritm.csv:
# 1) "C4.5"
# 2) "k - means"
# .....

import csv

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
             "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
             "Наивный байесовский классификатор", "CART" ]

try:
    with open("algoritm.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["id", "algoritm"])

        for i, name in enumerate(algoritm, start=1):
            writer.writerow([i, name])

    print("Файл algoritm.csv успешно создан")
except Exception as e:
    print(f"Возникла ошибка при записи файла: {e}")