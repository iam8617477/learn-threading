import threading
import time


res = list()


def load_file(file_name):
    thread_name = threading.current_thread().name
    res.append(f"{thread_name} начал загрузку файла {file_name}.")
    time.sleep(1)
    res.append(f"{thread_name} завершил загрузку файла {file_name}.")


def process_file(file_name):
    thread_name = threading.current_thread().name
    res.append(f"{thread_name} начал обработку файла {file_name}.")
    time.sleep(1)
    res.append(f"{thread_name} завершил обработку файла {file_name}.")


def save_file(file_name):
    thread_name = threading.current_thread().name
    res.append(f"{thread_name} начал сохранение файла {file_name}.")
    time.sleep(1)
    res.append(f"{thread_name} завершил сохранение файла {file_name}.")


file_names = ['file623.xlsx', 'file538.jpg', 'file13.txt']

ts = list()
for file_name in file_names:
    t1 = threading.Thread(target=load_file, args=(file_name,), name=f'LoadThread-{file_name}')
    t2 = threading.Thread(target=process_file, args=(file_name,), name=f'ProcessThread-{file_name}')
    t3 = threading.Thread(target=save_file, args=(file_name,), name=f'SaveThread-{file_name}')
    ts.append(t1)
    ts.append(t2)
    ts.append(t3)

list(map(lambda x: x.start(), ts))
list(map(lambda x: x.join(), ts))

for r in res:
    print(r)
