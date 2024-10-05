import threading
import time

code_names = ["Alpha", "Bravo"]


def task():
    time.sleep(1)
    print(f"Задача выполнена для {threading.current_thread().name}")


ts = list()


def main():
    for i, code_name in enumerate(code_names):
        thread = threading.Thread(target=task)
        thread.start()
        print(f"Исходное имя потока: {thread.name}")
        thread.name = code_name
        print(f"Новое имя потока: {thread.name}")
        ts.append(thread)

    _ = (t.join() for t in ts)

main()
