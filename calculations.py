from concurrent.futures import ThreadPoolExecutor

import math

# Функция для вычисления числа Фибоначчи
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Функция для вычисления суммы квадратных корней чисел в диапазоне
def sum_of_square_roots(start, end):
    total_sum = 0
    for i in range(start, end + 1):
        total_sum += math.sqrt(i)
    return round(total_sum, 4)

# Функция для вычисления факториала числа
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


with ThreadPoolExecutor(max_workers=3) as executor:

    # Отправка задач в пул потоков
    fib_future = executor.submit(fibonacci, 20)
    sqrt_future = executor.submit(sum_of_square_roots, 1, 50)
    fact_future = executor.submit(factorial, 20)

    fib_result = fib_future.result()
    sqrt_result = sqrt_future.result()
    fact_result = fact_future.result()

    print(f"20-е число Фибоначчи: {fib_result}")
    print(f"Сумма квадратных корней чисел от 1 до 50: {sqrt_result}")
    print(f"Факториал числа 20: {fact_result}")
