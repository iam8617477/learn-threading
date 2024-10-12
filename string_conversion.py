from concurrent.futures import ThreadPoolExecutor

strings = [
    "Да Здравствует ThreadPoolExecutor!!!",
    "Многопоточность в Python позволяет выполнять несколько задач одновременно, улучшая производительность.",
    "Многопоточность может увеличить сложность управления памятью и ресурсами.",
    "Правильное использование многопоточности в Python может значительно улучшить производительность приложений."
]


def to_uppercase(string: str):
    return string.upper()


futures = list()
with ThreadPoolExecutor(max_workers=3) as executor:
    for string in strings:
        future = executor.submit(to_uppercase, string)
        futures.append(future)

    for f in futures:
        print(f.result())
