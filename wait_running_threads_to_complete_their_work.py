import threading
import time


def f(start, end, sec):
    for i in range(start, end+1):
        print(i)
        time.sleep(sec)


thread1 = threading.Thread(target=f, args=(1, 5, 0.5))
thread2 = threading.Thread(target=f, args=(6, 10, 1))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('Оба потока завершили свою работу.')
