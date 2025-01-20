import threading
import time

dishes = {
    'Алексей': {'Маргарита': 3, 'Лазанья': 5, 'Креветочная': 4, 'Мидии в сливках': 4, 'Сицилийская': 5},
    'Марина': {'Мексиканская': 3, 'Вегетарианская': 4},

}

print_lock = threading.Lock()

locks = [threading.Lock() for _ in range(5)]


def bake(chief, dish, time_to_cook):
    with print_lock:
        print(f'{chief} начал(а) готовить {dish}, время приготовления {time_to_cook} сек.')
    time.sleep(time_to_cook)
    with print_lock:
        print(f'{chief} закончил(а) готовить {dish}, заняло {time_to_cook} сек.')


def cook_dish(chief, dishes):
    for dish, time_to_cook in dishes.items():
        # while True:
        #     for lock in locks:
        #         if not lock.locked():
        #             with lock:
        #                 bake(chief, dish, time_to_cook)
        #             break
        if not locks[0].locked():
            with locks[0]:
                bake(chief, dish, time_to_cook)
        elif not locks[1].locked():
            with locks[1]:
                bake(chief, dish, time_to_cook)
        elif not locks[2].locked():
            with locks[2]:
                bake(chief, dish, time_to_cook)
        elif not locks[3].locked():
            with locks[3]:
                bake(chief, dish, time_to_cook)
        else:
            with locks[4]:
                bake(chief, dish, time_to_cook)


def main(dishes):
    threads = []
    for chief, dishes in dishes.items():
        thread = threading.Thread(target=cook_dish, args=(chief, dishes))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


main(dishes)
