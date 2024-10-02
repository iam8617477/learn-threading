import threading

main_thread = threading.main_thread()
print(f'Имя главного потока по умолчанию: {main_thread.name}')
main_thread.name = 'My_main_thread'
print(f'Новое имя главного потока: {main_thread.name}')
print(f'Демонический признак главного потока: {main_thread.daemon}')
