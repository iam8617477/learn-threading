import time
from queue import Empty, Queue
from threading import Thread

elements = ['телевизор', 'холодильник', 'микроволновка', 'утюг', 'чайник',
            'пылесос', 'стиральная машина', 'кофеварка', 'фен', 'утюг']

def producer(queue, l):
    for i in l:
        queue.put(i)
        print(f'Добавлен: {i}')
        time.sleep(0.5)
    print(f'Все элементы добавлены')

def consumer(queue):
    while True:
        time.sleep(1)
        item = queue.get()
        print(f'Извлечен: {item}')
        queue.task_done()


def main():
    queue = Queue()

    # создаем поток-производитель и запускаем его
    producer_thread = Thread(target=producer, args=(queue, elements), daemon=True)
    producer_thread.start()

    # создаем поток-потребитель и запускаем его
    consumer_thread = Thread(target=consumer, args=(queue,), daemon=True)
    consumer_thread.start()

    # дожидаемся, пока все задачи добавятся в очередь
    producer_thread.join()

    # дожидаемся, пока все задачи в очереди будут завершены
    queue.join()
    print('Все элементы очереди обработаны')


if __name__ == '__main__':
    main()

