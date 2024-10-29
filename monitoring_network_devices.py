from concurrent.futures import ThreadPoolExecutor
from threading import Lock

lock = Lock()


def safe_print(*args, **kwargs):
    with lock:
        print(*args, **kwargs)

devices = [
    {"name": "Server1", "ip": "192.168.1.1", 'status': True},
    {"name": "Router1", "ip": "192.168.1.2", 'status': True},
    {"name": "Switch1", "ip": "192.168.1.3", 'status': False},
    {"name": "Server10", "ip": "192.168.1.28", 'status': True},
    {"name": "Router10", "ip": "192.168.1.29", 'status': False},
    {"name": "Switch10", "ip": "192.168.1.30", 'status': True}
]


def monitor_device(device):
    safe_print(f"Мониторинг устройства: {device['name']}, с IP {device['ip']} статус: {device['status']}")
    return device

# Функция обратного вызова для обработки результата мониторинга
def handle_device_status(future):
    device = future.result()
    if device['status']:
        safe_print(f"Устройство {device['name']} активно и работает нормально.")
    else:
        print(f"Внимание: Устройство {device['name']} неактивно! Включаем устройство.")
        device['status'] = True
        print(f"Устройство {device['name']} успешно включено!")


# Создание пула потоков
with ThreadPoolExecutor() as executor:
    for device in devices:
        f = executor.submit(monitor_device, device)
        f.add_done_callback(handle_device_status)
