# Функція для парсингу рядків логу.
# Приймає рядок логу та повертає словник з його складовими: дата, час, рівень та повідомлення.
def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

# Функція для завантаження логів з файлу.
# Приймає шлях до файлу логів та повертає список словників, які представляють кожен рядок логу.
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return logs

# Функція для фільтрації логів за рівнем.
# Приймає список логів та рівень логування, повертає список логів, що відповідають заданому рівню.
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper()]

# Функція для підрахунку записів за рівнем логування.
# Приймає список логів та повертає словник з кількістю записів для кожного рівня логування.
def count_logs_by_level(logs: list) -> dict:
    counts = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}
    for log in logs:
        if log['level'] in counts:
            counts[log['level']] += 1
    return counts

# Функція, яка форматує та виводить результати.
# Приймає словник з кількістю записів та виводить його у вигляді таблиці.
def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    
    # Сортуємо за кількістю (значеннями) в порядку спадання
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    for level, count in sorted_counts:
        print(f"{level:<16} | {count}")
