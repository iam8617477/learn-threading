import threading

# Массив чисел для обработки
numbers = [456, 467, 961, 561, 512, 740, 6412, 464, 444, 102, 456, 347, 905, 854, 901, 326, 267, 236, 790, 235, 745,
           769, 467, 734, 745, 895, 445, 312, 123, 451, 523, 567, 344, 234]

# Глобальные переменные для хранения сумм
sum_even = 0
sum_odd = 0


# Функция для суммирования четных чисел
def sum_even_numbers(numbers):
    global sum_even
    sum_even = sum(filter(lambda x: x%2 == 0,  numbers))


# Функция для суммирования нечетных чисел
def sum_odd_numbers(numbers):
    global sum_odd
    sum_odd = sum(filter(lambda x: x%2 != 0,  numbers))


# Создайте потоки
thread_even = threading.Thread(target=sum_even_numbers, args=(numbers, ))
thread_odd = threading.Thread(target=sum_odd_numbers, args=(numbers, ))

# Запустите потоки
thread_even.start()
thread_odd.start()

# Дождитесь завершения обоих потоков
thread_even.join()
thread_odd.join()

# Выводим результаты
print(f"Сумма четных чисел: {sum_even}")
print(f"Сумма нечетных чисел: {sum_odd}")
