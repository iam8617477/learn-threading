import threading

astronauts = ["Алексей Леонов", "Юрий Гагарин", "Джон Гленн"]
tasks = ["Ремонт оборудования", "Проведение экспериментов", "Мониторинг систем"]
intervals = [0.7, 1.3, 1.8]


def task(astronaut, task_name):
    print(f'{astronaut} выполняет задачу: {task_name}')


def space_station():
    for i, task_name in enumerate(tasks):
        threading.Timer(intervals[i], function=task, args=(astronauts[i], task_name, )).start()


space_station()
