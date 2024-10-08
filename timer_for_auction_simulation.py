import threading


def backup_data(backup_):
    print("Выполнение резервного копирования данных.")
    # имитация резервного копирования
    backup_()


def backup():
    # Планирование резервного копирования через каждые 24 часа (86400 секунд)
    timer = threading.Timer(2, backup_data, args=(backup, ))
    timer.start()

backup_data(backup)
