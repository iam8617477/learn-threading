import threading
import time


def my_func(i):
    print(f"Поток {i} начал выполняться")
    time.sleep(1)
    print(f"Поток {i} закончил свое выполнение")


threads = []

for i in range(1, 4):
    thread = threading.Thread(target=my_func, args=(i,))
    threads.append(thread)

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"{threading.main_thread().name} продолжает свое выполнение")
