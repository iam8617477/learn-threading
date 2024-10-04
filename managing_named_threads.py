import threading
import time

name_threads = ['OF95RK', 'VH61DX', 'NB03WA', 'WO40ZF', 'NJ48EG', 'SX21ET', 'AT01PA', 'MR36DD', 'DD84HR', 'MI81QY']


def worker():
    print(f'{threading.current_thread().name} начал работу.')
    time.sleep(1)
    print(f'{threading.current_thread().name} завершил работу.')


ts = list()
for name_thread in name_threads:
    t = threading.Thread(target=worker, name=f'Name_thread-{name_thread}')
    t.start()
    ts.append(t)

list(t.join() for t in ts)
