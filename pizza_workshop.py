import threading
import time

# Создаем объект мьютекса
oven_lock = threading.Lock()

# Список видов пицц и время их приготовления
pizzas = {
    "Маргарита": 3,
    "Пепперони": 2,
    "Вегетарианская": 4,
    "Четыре сыра": 5,
    "Гавайская": 3
}
pizzas = tuple(pizzas.items())
# Список имен поваров
cooks_names = ["Алексей", "Марина", "Сергей", "Ирина", "Николай"]


def cook_pizza(cook_name, pizza_name, time_to_cook):
    with oven_lock:
        print(f'{cook_name} начал(а) готовить пиццу "{pizza_name}".')
        time.sleep(time_to_cook)
        print(f'{cook_name} закончил(а) готовить пиццу "{pizza_name}".')


def main():
    threads = list()
    for cooks_name, pizza in zip(cooks_names, pizzas):
        pizza_name, time_to_cook = pizza
        thread = threading.Thread(target=cook_pizza, args=(cooks_name, pizza_name, time_to_cook))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print('Все пиццы приготовлены!')

main()
