import threading


def client_behavior(client_name, ready_event):
    print(f"{client_name} вошел в банк")
    ready_event.set()
    print(f"{client_name} обслужен и покидает банк")


def cashier_work(client_name, ready_event):
    ready_event.wait()
    print(f"Обслуживаю клиента {client_name}")
    print(f"Клиент {client_name} обслужен")


if __name__ == "__main__":
    clients = ["Виктор", "Ирина", "Андрей"]
    threads = []
    events = []

    for client in clients:
        ready_event = threading.Event()
        events.append(ready_event)

        t_client = threading.Thread(target=client_behavior, args=(client, ready_event))
        threads.append(t_client)

        t_cashier = threading.Thread(target=cashier_work, args=(client, ready_event))
        threads.append(t_cashier)

        t_client.start()
        t_cashier.start()

    for t in threads:
        t.join()

    print("Все клиенты обслужены. Банк закрывается.")
