#todo: Допишите для игры "Поле чудес" функции сохранения и загрузки игры через сериализацию.
# Данные сериализации записываются и сохраняются в файле.

import  random
import json
import os
from datetime import datetime

_dict = {
    'False': 'Логическое значение, противоположное истине',
    'None': 'Пустое значение в Python',
    'List': 'Изменяемая упорядоченная коллекция объектов',
    'Dict': 'Словарь, хранит пары ключ-значение',
    'Tuple': 'Неизменяемая упорядоченная коллекция'
}

NUM_SAVES = 5
secret = ""
mask = []
current_slot = None

def init_new_game():
    """Инициализирует новую игру, выбирая случайное слово."""
    global secret, mask
    keys = list(_dict.keys())
    ind = random.randint(0, len(keys) - 1)
    secret = keys[ind]
    mask = [' * '] * len(secret)


def get_slot_filename(slot_num):
    """Возвращает имя файла для указанного слота."""
    return f"save_slot_{slot_num}.json"

def save_game(slot_num):
    """Сериализует и сохраняет текущее состояние игры в указанный слот."""
    global secret, mask, current_slot

    game_state = {
        "secret": secret,
        "mask": mask,
        "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "progress": f"{mask.count(' * ')} букв осталось"
    }

    filename = get_slot_filename(slot_num)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(game_state, f, ensure_ascii=False, indent=4)

    current_slot = slot_num
    print(f"\nИгра сохранена в слот {slot_num}!")


def load_game(slot_num):
    """Загружает состояние игры из указанного слота."""
    global secret, mask, current_slot

    filename = get_slot_filename(slot_num)

    if not os.path.exists(filename):
        print(f"\nСлот {slot_num} пуст!")
        return False

    try:
        with open(filename, "r", encoding="utf-8") as f:
            game_state = json.load(f)

        secret = game_state["secret"]
        mask = game_state["mask"]
        current_slot = slot_num

        print(f"\nИгра загружена из слота {slot_num}!")
        print(f"Сохранено: {game_state['saved_at']}")
        return True
    except (json.JSONDecodeError, KeyError):
        print(f"\nОшибка чтения слота {slot_num}. Файл поврежден.")
        return False


def show_save_slots():
    """Показывает информацию о всех слотах сохранений."""
    print("\n" + "=" * 60)
    print("Слоты сохранений")
    print("=" * 60)

    for slot in range(1, NUM_SAVES + 1):
        filename = get_slot_filename(slot)
        print(f"\n[Слот {slot}]: ", end="")

        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    game_state = json.load(f)

                mask_display = "".join(game_state["mask"])
                print(f"{mask_display}")
                print(f"   Сохранено: {game_state['saved_at']}")
                print(f"   Прогресс: {game_state['progress']}")
            except Exception as e:
                print("(файл поврежден)")
        else:
            print("(пусто)")

    print("\n" + "=" * 50)


def show_load_menu():
    """Показывает меню выбора слота для загрузки."""
    show_save_slots()

    while True:
        choice = input(f"\nВыберите слот для загрузки (1-{NUM_SAVES}) или '0' для отмены: ").strip()

        if choice == '0':
            return None

        list_punkts = []
        for i in range(1, NUM_SAVES + 1):
            list_punkts.append(str(i))

        if choice in list_punkts:
            slot_num = int(choice)
            filename = get_slot_filename(slot_num)

            if os.path.exists(filename):
                return slot_num
            else:
                print(f"Слот {slot_num} пуст! Выберите другой или создайте новое сохранение.")
        else:
            print(f"Введите число от 0 до {NUM_SAVES}.")


def show_save_menu():
    """Показывает меню выбора слота для сохранения."""
    show_save_slots()

    while True:
        choice = input(f"\nВыберите слот для сохранения (1-{NUM_SAVES}) или '0' для отмены: ").strip()

        if choice == '0':
            return None

        list_punkts = []
        for i in range(1, NUM_SAVES + 1):
            list_punkts.append(str(i))

        if choice in list_punkts:
            slot_num = int(choice)
            filename = get_slot_filename(slot_num)

            if os.path.exists(filename):
                confirm = input(f"Слот {slot_num} уже занят. Перезаписать? (д/н): ").strip().lower()
                if confirm not in ['д', 'y', 'yes']:
                    continue

            return slot_num
        else:
            print(f"Введите число от 0 до {NUM_SAVES}.")


def show_describe():
    """ Выводит описание слова  """
    print(_dict[secret])


def show_secret():
    """ Выводит слово """
    for val in mask:
       print(val, end="")


def get_letter():
    letter = input("\n Введите букву или save, чтобы сохранить игру или exit, чтобы выйти:")
    return letter


def check_letter(letter):
    found = False
    for ind, val in enumerate(secret):
        if val.upper() == letter.upper():
            mask[ind] = f" {letter} "
            found = True
    return "Такая буква есть" if found else "Такой буквы нет"


def start():
    choice = None
    while choice != "3":
        while True:
            print("Главное меню")
            print("1. Начать новую игру")
            print("2. Загрузить сохранение")
            print("3. Выход")

            choice = input("\nВведите пункт меню: ").strip()

            if choice == '1':
                init_new_game()
                break
            elif choice == '2':
                slot_num = show_load_menu()
                if slot_num is not None:
                    if load_game(slot_num):
                        break
            elif choice == '3':
                print("\nДо свидания!")
                return
            else:
                print("Введите пункт меню от 1 до 3.")

        while " * " in mask:
            show_describe()
            show_secret()

            letter = get_letter()

            if letter.lower() in ['сохранить', 'save']:
                slot_num = show_save_menu()
                if slot_num is not None:
                    save_game(slot_num)
                continue

            if letter.lower() in ['exit', 'выход']:
                break

            if len(letter) > 1 and letter.lower() not in ['сохранить', 'save', 'с']:
                print("Пожалуйста, вводите по одной букве.")
                continue

            if letter:
                check_letter(letter)

        print(f"Вы отгадали слово: {secret.upper()}")

        # if current_slot is not None:
        #     filename = get_slot_filename(current_slot)
        #     if os.path.exists(filename):
        #         os.remove(filename)
        #         print(f"\nСлот {current_slot} очищен.")

start()
