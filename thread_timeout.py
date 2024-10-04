import threading
import time


def main(sec):
    print(f'Поток {threading.current_thread().name} запустился.')
    time.sleep(sec)


ts = list()
t1 = threading.Thread(target=main, args=(2,), name='A')
t2 = threading.Thread(target=main, args=(3,), name='B')
t1.start(), t2.start()
ts.extend([t1, t2])
time.sleep(2.1)
for t in ts:
    if t.is_alive():
        print(f'Поток {t.name} не завершился за установленное время.')
