from helpers import logger, caesar_cipher

print("=" * 50)
print("Тест логгера")
print("=" * 50)

logger("Приложение запущено")
logger("Загрузка данных...", "INFO")
logger("Предупреждение: медленное соединение", "WARNING")
logger("Ошибка подключения к базе данных", "ERROR")

print("\nЛог записан в файл app.log")

print("Тест шифра Цезаря")

original_text = "Привет, мир!"

print(f"\nИсходный текст: {original_text}")

encrypted = caesar_cipher(original_text, "encrypted_message.txt")
print(f"Зашифрованный текст: {encrypted}")
