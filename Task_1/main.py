def caching_fibonacci() -> callable:
    # Створюємо пустий словник для зберігання результатів обчислення чисел Фібоначчі
    cache = {}

    # Визначаємо внутрішню функцію fibonacci, яка буде використовувати кеш
    def fibonacci(n: int) -> int:
        #  Якщо n менше або дорівнює 0, то повертаємо 0
        if n <= 0:
            return 0
        # Якщо n дорівнює 1, то повертаємо 1
        elif n == 1:
            return 1
        # Перевіряємо чи значення вже є в кеші та повертаємо його
        if n in cache:
            return cache[n]

        # Інакше обчислюємо значення і зберігаємо його в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Повертаємо обчислене значення
        return cache[n]

    # Повертаємо функцію fibonacci як замикання, яка запам'ятала словник cache
    return fibonacci

# Отримуємо функцію fibonacci з кешуванням
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610