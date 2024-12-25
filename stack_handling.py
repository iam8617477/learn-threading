import threading
from queue import LifoQueue


# Функция для извлечения элементов из стека
def process_stack(item):
    print(f'Обработка элемента: {item}')


def process_tasks(queue):
    while True:
        task_id = queue.get()
        process_stack(task_id)
        queue.task_done()

# Создание стека и добавление в него элементов
queue = LifoQueue()
data = [15, 13, 7, 19, 3, 1, 11, 5, 9, 17]
for i in data:
    queue.put(i)


# Создание и запуск потоков для обработки стека
for _ in range(3):
    worker = threading.Thread(target=process_tasks, args=(queue,))
    worker.daemon = True
    worker.start()


# Ожидание завершения всех потоков
queue.join()

print('Все элементы успешно обработаны')
