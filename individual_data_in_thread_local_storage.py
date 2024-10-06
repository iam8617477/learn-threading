import threading
import time

students_info = {'Варлаам Бирюкова': {'Возраст': 25, 'Специальность': None, 'Город': None, 'Страна': 'Россия',
                                      'Университет': 'ЗАО «Миронова-Прохоров»', 'Курс': 3, 'Группа': 'CK008',
                                      'Электронная почта': 'ostaplitkin@example.com', 'Телефон': None,
                                      'Дата рождения': '2005-08-22', 'Пол': 'Женский',
                                      'Хобби': ['Физика', 'Астрономия'], 'Время обработки': 6},
                 'Никандр Мамонтов': {'Возраст': 20, 'Специальность': 'Компьютерные науки',
                                      'Город': 'к. Октябрьский (Башк.)', 'Страна': 'Россия', 'Университет': None,
                                      'Курс': 3, 'Группа': 'LE057', 'Электронная почта': 'jakub_2001@example.org',
                                      'Телефон': '+7 919 424 9512', 'Дата рождения': '2002-01-13', 'Пол': None,
                                      'Хобби': None, 'Время обработки': 5},}

local = threading.local()


def thread_function(student_name, student_info, sec):
    time.sleep(sec / 10)
    local.sleep_time = sec
    local.data = student_info
    for key, value in local.data.items():
        if value is not None:
            print(f"Имя потока - {student_name}, локальные данные потока - {key}: {value}")


ts = list()

for name, description in students_info.items():
    if description.get('Время обработки'):
        t = description.get('Время обработки')
    else:
        t = 3
    thread = threading.Thread(
        target=thread_function,
        args=(name, description, t),
        name=name
    )
    ts.append(thread)

for t in ts:
    t.start()

for t in ts:
    t.join()
