import random
import threading
import time

missions = {
    "Thread-Scan": "Сканирование данных",
    "Thread-Hack": "Взлом системы",
}


def mission(mission_name):
    print(f"[{mission_name}] Миссия началась.")
    time.sleep(random.randint(1, 3))
    print(f"[{mission_name}] Миссия успешно выполнена!")


ts = list()


def main():
    for thread_name, mission_name in missions.items():
        thread = threading.Thread(target=mission, args=(mission_name, ), name=thread_name)
        print(f"[{thread_name} ({mission_name})] Статус миссии до запуска: {thread.is_alive()}")
        thread.start()
        print(f"[{thread_name} ({mission_name})] Миссия активна: {thread.is_alive()}")
        ts.append(thread)

    list((t.join() for t in ts))

    for thread in ts:
        print(f"[{thread.name} ({missions[thread.name]})] Статус миссии после завершения: {not thread.is_alive()}")

main()
