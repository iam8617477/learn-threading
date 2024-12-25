from concurrent.futures import ThreadPoolExecutor
import time
data = [('CPU', 3.1), ('RAM', 1.5), ('GPU', 1.6), ('Motherboard', 1.8), ('SSD', 1.3),
        ('Keyboard', 1.5), ('Mouse', 3.9), ('Monitor', 2.8), ('Headphones', 3.0), ('Router', 1.0)]
def task(args):
    n, t = args
    time.sleep(t)
    print(f'Задача {n} выполнилась за {t} секунды')

with ThreadPoolExecutor(max_workers=5) as executor:
    fs = [executor.submit(task, item) for item in data]
    for f in fs:
        f.cancel()
