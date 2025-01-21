import threading
import time


condition = threading.Condition()
print_lock = threading.Lock()

clients_name = ["Алиса", "Владимир", "Сергей"]


def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)


def barista(orders):
    for order in orders:
        safe_print(f'Готовим кофе для {order}')
        with condition:
            safe_print(f'Кофе для {order} готов')
            condition.notify()
        time.sleep(3)


def client(name):
    safe_print(f'{name} зашел в кафе')
    with condition:
        condition.wait()
    safe_print(f'{name} получил свой кофе')


thread_clients = list()
for client_name in clients_name:
    thread = threading.Thread(target=client, args=(client_name, ))
    thread_clients.append(thread)
    thread.start()


thread_barista = threading.Thread(target=barista, args=(clients_name, ))
thread_barista.start()


for thread_client in thread_clients:
    thread_client.join()

thread_barista.join()

print('Все посетители получили свой кофе. Работа завершена.')
