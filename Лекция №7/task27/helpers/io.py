from datetime import datetime

def logger(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}"
    print(log_entry)

    # Опционально: запись в файл
    with open("app.log", "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")
