# Импортируйте все необходимое
import threading

result_sum = 0
result_mul = 1


# Напишите необходимые функции для вычисления суммы и произведения
def sum_all_numbers(start, end):
    global result_sum
    result_sum = sum(number for number in range(start, end))


def mul_all_numbers(start, end):
    global result_mul
    for i in range(start, end):
        result_mul *= i


# Создайте и запустите потоки с целевыми функциями
thread_sum = threading.Thread(target=sum_all_numbers, args=(1, 1001))
thread_mul = threading.Thread(target=mul_all_numbers, args=(1, 11))

thread_sum.start()
thread_mul.start()

thread_sum.join()
thread_mul.join()


# Выведите результаты работы потоков согласно условиям задачи
print(f"Сумма чисел от 1 до 1000: {result_sum}")
print(f"Произведение чисел от 1 до 10: {result_mul}")
