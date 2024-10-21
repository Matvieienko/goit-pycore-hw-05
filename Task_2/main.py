import sys
import re
from typing import Callable

# Встановлюємо кодування на utf-8 для коректного виведення
sys.stdout.reconfigure(encoding='utf-8')

# Функція, яка повертає генератор для знаходження чисел
def generator_numbers(text: str):
    # Використовуємо регулярний вираз для пошуку дійсних чисел з двома знаками після крапки
    # '\b' - межа слова, '\d+' - одна або більше цифр до крапки, '\.' - крапка, '\d{2}' - дві цифри після крапки
    pattern = r"\b\d+\.\d{2}\b" 
    matches = re.findall(pattern, text)
    
    # Проходимо по всіх знайдених числах і перетворюємо їх у float
    for match in matches:
        yield float(match)

# Функція для підсумовування всіх чисел, знайдених генератором
def sum_profit(text: str, func: Callable):
    # Використовуємо функцію генератор для знаходження чисел
    return sum(func(text))

# Тестуємо на прикладі
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
