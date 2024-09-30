import threading

# Список для суммирования
numbers = [123456, 7890123, 987654, 114455, 995423, 1000000]

# Глобальная переменная для хранения результата
total_sum = 0


# Функция для вычисления суммы элементов списка
def sum_number(numbers):
    return sum(numbers)


# Функция для потока, обрабатывающего список
def thread_task(numbers, sum_number):
    global total_sum
    total_sum = sum_number(numbers)


# Создайте поток
thread = threading.Thread(target=thread_task, args=(numbers, sum_number))

# Запустите поток
thread.start()

# Дождитесь завершения потока
thread.join()

# Напечатайте сумму списка numbers
print(total_sum)
