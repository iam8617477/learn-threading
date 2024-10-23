from concurrent.futures import ThreadPoolExecutor

list1 = [16, 10, 1]
list2 = [0, 7, 2]
list3 = [8, 19, 3]
list4 = [1, 0, 4]


def multiply_numbers(numbers):
    result = 1
    for number in numbers:
        if number == 0:
            raise ValueError("Обнаружено умножение на ноль")
        result *= number
    return result


with ThreadPoolExecutor() as executor:
    fs = [executor.submit(multiply_numbers, (list1[i], list2[i], list3[i], list4[i], )) for i in range(len(list1))]
    for f in fs:
        if f.exception() is not None:
            print(f"Обработано исключение: {f.exception()}")
        else:
            print(f"Результат: {f.result()}")
