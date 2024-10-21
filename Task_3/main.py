from functions import parse_log_line, load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts
import sys

# Основна функція, яка виконує аналіз логів.
# Зчитує аргументи командного рядка, завантажує логи, підраховує кількість записів
# та виводить результати. Якщо вказано рівень, виводить деталі логів для цього рівня.
def main():
    if len(sys.argv) < 2:
        print("Please provide a path to the log file.")
        return
    
    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None
    
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

# Запускаємо основну функцію, якщо скрипт викликається напряму.
if __name__ == "__main__":
    main()
