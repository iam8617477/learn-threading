import os
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests


def process_file(file_path):
    try:
        with open(file_path, "r") as file:
            url = file.readline().strip()
        if not url:
            print(f"Файл {file_path} пуст или не содержит ссылок.")
            return None
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        secret_code_div = soup.find("div", class_="secret-code")
        if secret_code_div:
            code = secret_code_div.find("p").get_text(strip=True)
            print(f"Секретный код найден: {code} (Источник: {file_path})")
            return code
    except requests.RequestException as e:
        print(f"Ошибка при обработке {file_path} (URL: {url}): {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка в {file_path}: {e}")

    return None


def find_secret_code_in_files(directory):
    
    if not os.path.isdir(directory):
        print(f"Директория {directory} не существует.")
        return
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(process_file, files))

    for code in results:
        if code:
            print(f"\nИтоговый секретный код: {code}")
            break
    else:
        print("\nСекретный код не найден ни в одном из файлов.")


directory_path = "files_6_1"
find_secret_code_in_files(directory_path)
