from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

lock = Lock()

def safe_print(*arg, **kwargs):
    with lock:
        print(*arg, **kwargs)

products = {
    1: {"name": "Компьютер ProMax", "price": 50000, "stock": 5},
    2: {"name": "Телефон UltraTalk", "price": 30000, "stock": 1},
    3: {"name": "Наушники SoundBeats", "price": 2000, "stock": 0},
    4: {"name": "Планшет ViewTab", "price": 15000, "stock": 20},
    5: {"name": "Монитор ClearView", "price": 10000, "stock": 15},
    6: {"name": "Клавиатура QuickType", "price": 1500, "stock": 30},
    7: {"name": "Мышь Clicker", "price": 800, "stock": 40},
    8: {"name": "Флешка SpeedDrive", "price": 500, "stock": 0},
    9: {"name": "Жесткий диск StoreMore", "price": 4000, "stock": 25},
    10: {"name": "Принтер PrintAll", "price": 6000, "stock": 12},
    11: {"name": "Смартфон FlexPhone", "price": 25000, "stock": 18},
    12: {"name": "Ноутбук CarryComp", "price": 45000, "stock": 8},
    13: {"name": "Камера SnapShot", "price": 8000, "stock": 22},
    14: {"name": "Проектор LightShow", "price": 12000, "stock": 0},
    15: {"name": "Спикеры SoundWave", "price": 2500, "stock": 35},
    16: {"name": "Монопод SelfieStick", "price": 700, "stock": 60},
    17: {"name": "Роутер NetFast", "price": 3000, "stock": 28},
    18: {"name": "Планшет SketchTab", "price": 13000, "stock": 0},
    19: {"name": "Микрофон EchoMic", "price": 1500, "stock": 45},
    20: {"name": "Веб-камера VisionPro", "price": 2000, "stock": 0},
    21: {"name": "Наушники BassHead", "price": 1800, "stock": 55},
    22: {"name": "Мышь для геймеров GameMaster", "price": 1200, "stock": 38},
    23: {"name": "Клавиатура для геймеров KeyStrike", "price": 2500, "stock": 0},
    24: {"name": "Графический планшет DrawMaster", "price": 8000, "stock": 17},
    25: {"name": "Смарт-часы TimeTech", "price": 3000, "stock": 23},
    26: {"name": "Компьютерные колонки SoundSpace", "price": 3500, "stock": 30},
    27: {"name": "Беспроводная мышь FreedomClick", "price": 1000, "stock": 42},
    28: {"name": "Смартфон Samsung GalaxyZ", "price": 27000, "stock": 0},
    29: {"name": "Смартфон iPhone X", "price": 35000, "stock": 9},
    30: {"name": "Ноутбук Dell Inspire", "price": 48000, "stock": 7},
}


def search_product(product_id):
    global products

    product = products.get(product_id)
    if product is not None:
        product_name = product['name']
        product_stock = product.get('stock')
        if product_stock is not None and product_stock > 0:
            safe_print(f"Поиск товара: {product_name}")
            safe_print(f"Товар ID {product_id}: {product}")
            return product
    safe_print(f"Товар ID {product_id} не найден или закончился на складе.")


def task_callback(future):
    safe_print(f"Поиск завершён, статус: {future.done()}")


with ThreadPoolExecutor(max_workers=len(products)) as executor:
    fs = list()
    for product_id in products.keys():
        f = executor.submit(search_product, product_id)
        f.add_done_callback(task_callback)
        fs.append(f)

    total_cost = list()
    for f in as_completed(fs):
        result = f.result()
        if result is not None:
            total_cost.append(result['price']*result['stock'])

print(f'Общая стоимость товаров на складе: {sum(total_cost)}')
