import queue
import threading
import time

# Блокировка для потокобезопасного вывода в консоль.
lock = threading.Lock()

electronics = [(1, "смартфон"), (15, "ноутбук"), (7, "планшет"), (33, "камера"), (67, "гарнитура"),
               (4, "телевизор"), (21, "гаджет"), (83, "монитор"), (0, "роутер"), (47, "плеер")]


# Приоритетная очередь.
priority_queue = queue.PriorityQueue(maxsize=5)


# Функция для извлечения элемента очереди
def extractor(_queue):
    while True:
        priority, el = _queue.get()
        time.sleep(priority / 100)
        with lock:
            print(f'Обработан "{el}"')
        _queue.task_done()


# Функция для постановки элемента в очередь
def loader(_queue, seq):
    for el in seq:
        _queue.put(el)


# Создаем 2 потока которые будут обслуживать очередь.
for i in range(2):
    t = threading.Thread(target=extractor, args=(priority_queue,), daemon=True)
    t.start()

producer_thread = threading.Thread(target=loader, args=(priority_queue, electronics,), daemon=True)
producer_thread.start()

# Блокируем выполнение программы до выполнения всех заданий в очереди
priority_queue.join()
