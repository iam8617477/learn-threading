import threading
import random
import time


waiters = ["Анна", "Иван", "Света"]
chefs = ["Шеф_Антон", "Шеф_Сергей", "Шеф_Георгий"]
dishes = ["Борщ", "Салат Цезарь", "Стейк", "Паста Карбонара", "Тирамису"]


orders = []
condition = threading.Condition()
print_lock = threading.Lock()  
work_done = False  


def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)


def waiter(waiter_name):
    for _ in range(3):  
        time.sleep(random.randint(1, 3))  
        dish = random.choice(dishes)
        with condition:
            orders.append(dish)
            safe_print(f"{waiter_name} передал заказ на {dish}")
            condition.notify()  


def chef(chef_name):
    while True:
        with condition:
            while not orders and not work_done:  
                condition.wait()
            if work_done and not orders:  
                break
            dish = orders.pop(0)  
        
        safe_print(f"{chef_name} готовит {dish}...")
        time.sleep(random.randint(1, 3))
        safe_print(f"{chef_name} закончил готовить {dish}")


def main():
    global work_done
    waiter_threads = [threading.Thread(target=waiter, args=(name,)) for name in waiters]
    chef_threads = [threading.Thread(target=chef, args=(name,)) for name in chefs]

    for thread in waiter_threads:
        thread.start()

    for thread in chef_threads:
        thread.start()

    for thread in waiter_threads:
        thread.join()

    with condition:
        work_done = True
        condition.notify_all()

    for thread in chef_threads:
        thread.join()


if __name__ == "__main__":
    main()
