import time
from concurrent.futures import ThreadPoolExecutor

data = [(1, "Python"), (2, "Java"), (3, "Go"), (4, "JavaScript"), (5, "C++"),
        (6, "TypeScript"), (7, "PHP"), (8, "Ruby"), (9, "C"), (10, "C#")]


def f(rate: tuple):
    rate, language = rate
    time.sleep(rate/10)
    return f"{language} на {rate}-м месте на GitHub в первом квартале 2024 года"


with ThreadPoolExecutor(len(data)) as executor:
    for f in executor.map(f, data):
        print(f)
