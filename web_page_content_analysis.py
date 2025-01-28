from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


def fetch_word_count(link):
    print(f'Fetching link {link}')
    try:
        response = requests.get(link, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        page_text = soup.get_text()
        word_count = len(page_text.split())
        return word_count
    except requests.RequestException:
        return 0  


def count_words_in_links_threaded(file_path):
    try:
        with open(file_path, "r") as file:
            links = [line.strip() for line in file if line.strip()]

        with ThreadPoolExecutor(max_workers=40) as executor:
            results = executor.map(fetch_word_count, links)

        total_word_count = sum(results)
        print(f"\nОбщее количество слов на всех страницах: {total_word_count}")

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")


file_path = "generated_links.txt"
count_words_in_links_threaded(file_path)
