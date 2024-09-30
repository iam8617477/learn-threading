import threading

# Глобальные переменные для массивов
array_descending = [725, 733, 389, 606, 544, 526, 496, 448, 345, 239]
array_ascending = [124, 168, 350, 501, 389, 419, 428, 662, 760, 829]
symbols_array = ['g', 'e', 'k', 'a', 'w', 'z', 'o', 'b', 'm', 'l', 'h', 'n', 'd', 's', 'q']


# Функции для сортировки массивов
def sort_numbers_descending():
    #Допишите функцию сортировки массива по убыванию
    global array_descending
    array_descending = sorted(array_descending, reverse=True)



def sort_numbers_ascending():
    #Допишите функцию сортировки массива по возрастанию
    global array_ascending
    array_ascending = sorted(array_ascending)


def sort_symbols():
    #Допишите функцию сортировки массива символов в лексикографическом порядке
    global symbols_array
    symbols_array = sorted(symbols_array)


# Создайте и запустите потоки для сортировки
thread1 = threading.Thread(target=sort_symbols)
thread2 = threading.Thread(target=sort_numbers_ascending)
thread3 = threading.Thread(target=sort_numbers_descending)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

# Выведете отсортированные массивы
print(f"Массив чисел (по убыванию): {array_descending}")
print(f"Массив чисел (по возрастанию): {array_ascending}")
print(f"Массив символов (лексикографический порядок): {symbols_array}")
