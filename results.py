from concurrent.futures import ThreadPoolExecutor, TimeoutError, as_completed
# Функция для подсчета символов в строке
messages = [
    "Привет, давайте обсудим многопоточность в Python!",
    "Да, GIL - это большая проблема для многопоточности в Python.",
]
def count_characters(message):
    return len(message)

# Использование ThreadPoolExecutor для параллельного подсчета символов
with ThreadPoolExecutor(max_workers=5) as executor:
    character_counts = executor.map(count_characters, messages)
# Вывод результатов
print(f"Общее количество символов в каждой строке: {list(character_counts)}")
