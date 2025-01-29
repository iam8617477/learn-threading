from concurrent.futures import ThreadPoolExecutor, as_completed

# Словарь с оценками студентов
# Полный словарь вшит в задачу
students_grades = {
    "Иван": [5, 4, 3, 5],
    "Алексей": [],
    "Мария": [5, 5, 5, 5],
    "Андрей": [4, 4, 3, 5],
    "Екатерина": [3, 4, 5, 4],
    "Петр": [5, 5, 4, 4],
    "Наталья": [3, 4, 4, 3],
    "Сергей": [4, 4, 4, 5],
    "Анна": [5, 4, 5, 5],
    "Дмитрий": [],
    "Елена": [3, 4, 4, 3],
    "Алина": [5, 5, 5, 5],
    "Артем": [4, 4, 5, 4],
    "Ольга": [5, 4, 3, 5],
    "Ирина": [4, 3, 5, 5],
    "Константин": [],
    "Татьяна": [3, 4, 5, 5],
    "Владимир": [4, 4, 5, 4],
    "Юлия": [5, 5, 5, 5],
    "Валентин": [],
    "Светлана": [3, 4, 3, 3],
    "Виктор": [5, 4, 5, 5],
    "Галина": [4, 4, 4, 4],
    "Роман": [5, 4, 5, 4],
    "Михаил": [4, 4, 5, 4],
    "Оксана": [],
    "Лариса": [4, 4, 3, 5],
    "Даниил": [5, 5, 5, 5],
    "Максим": [4, 4, 5, 4],
    "Валерия": [3, 3, 4, 4]
}


def calculate_average_grade(student, grades):
    if grades:
        average = sum(grades)/len(grades)
        return f"Средний балл {student}: {average:.2f}"
    else:
        raise ValueError(f"У студента {student} нет оценок.")


def main():
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(calculate_average_grade, student, grades) for student, grades in students_grades.items()
        ]
        for future in as_completed(futures):
            try:
                print(future.result())
            except ValueError as e:
                print(str(e))


main()
