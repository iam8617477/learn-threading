from concurrent.futures import ThreadPoolExecutor
from threading import Lock

lock = Lock()


def safe_print(*args, **kwargs):
    with lock:
        print(*args, **kwargs)

inventory = {
            'Intel Core i9': 120,
            'Intel Core i7': 66,
            'Intel Core i5': 60,
            'Intel Core i3': 1,
            'Intel Xeon': 81,
            'AMD Ryzen 9': 56,
            'AMD Ryzen 7': 55,
            'AMD Ryzen 5': 0,
            'AMD Ryzen 3': 1,
            'AMD Threadripper': 41,
            'AMD Epyc': 3,
            'Intel Pentium': 19,
            'Intel Celeron': 2,
            'Qualcomm Snapdragon 888': 54,
            'Apple M1': 14,
            'Apple A14 Bionic': 20,
            'ARM Cortex-A78': 0,
            'ARM Cortex-A55': 87,
            'ARM Cortex-M4': 30,
            'NVIDIA Tegra X1': 2,
            'Samsung Exynos 2100': 22,
            'MediaTek Dimensity 1000': 0,
            'Intel Atom': 0, 'AMD Athlon': 95,
            'AMD Sempron': 30,
            'Intel Core 2 Duo': 2,
            'Intel Core 2 Quad': 1,
            'Intel Itanium': 2,
            'AMD Duron': 98, 'AMD FX': 0
}


# Функция для обработки каждого элемента словаря
def process_item(item_id):
    global inventory
    safe_print(f"Поиск товара {item_id}. Количество на складе: {inventory[item_id]} шт")
    processed = False
    if inventory[item_id] > 0:
        inventory[item_id] -= 1
        processed = True

    return item_id, inventory[item_id], processed


# Функция обратного вызова для проверки оставшегося количества
def check_inventory(future):
    item_id, remaining, processed = future.result()
    if processed:
        safe_print(f"Товар отправлен получателю {item_id}. Осталось {remaining}")
    else:
        safe_print(f"Товара {item_id} нет в наличии, обработка невозможна.")


# Использование ThreadPoolExecutor для обработки каждого элемента словаря
with ThreadPoolExecutor() as executor:
    for item in inventory.keys():
        f = executor.submit(process_item, item)
        f.add_done_callback(check_inventory)
