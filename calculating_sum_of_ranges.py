from concurrent.futures import ThreadPoolExecutor


def sum_range(start, end):
    return sum(range(start, end + 1))


with ThreadPoolExecutor(max_workers=3) as executor:
    futures1 = executor.submit(sum_range, 1, 100)
    futures2 = executor.submit(sum_range, 101, 200)
    futures3 = executor.submit(sum_range, 201, 300)
    sum1 = futures1.result()
    sum2 = futures2.result()
    sum3 = futures3.result()

    print(f"Сумма чисел от 1 до 100: {sum1}")
    print(f"Сумма чисел от 101 до 200: {sum2}")
    print(f"Сумма чисел от 201 до 300: {sum3}")
