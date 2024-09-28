import time
from threading import Thread, current_thread


def task0():
    for i in range(1, 6):
        print(i)


def countdown():
    for i in range(5, 0, -1):
        print(f'Need {i} sec')
        time.sleep(1)


def task():
    task_thread_id = current_thread().ident
    time.sleep(1)
    print(f'task from {task_thread_id}')


start = time.time()
base_thread_id = current_thread().ident
print(f'id main tread: {base_thread_id}')
thread = Thread(target=task)
print('run new thread')
thread.start()
print('need new thread')
time.sleep(1)
thread.join()
print('new thread is finished')
print(f'program time: {time.time() - start:.4f} sec')
