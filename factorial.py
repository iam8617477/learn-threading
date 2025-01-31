from multiprocessing.pool import ThreadPool


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


numbers = [5, 3, 7, 11, 17, 23, 25, 29, 30]


def calculate_factorial(numbers):
    with ThreadPool() as pool:
        results = [pool.apply(factorial, (num,)) for num in numbers]

    for num, fact in zip(numbers, results):
        print(f"Factorial of {num} is {fact}")


calculate_factorial(numbers)