import threading
from concurrent.futures import ThreadPoolExecutor
import json

lock = threading.Lock()


def read_specific_line(file_name, line_number):
    with open(file_name, 'r', encoding='utf-8') as file:
        for current_line, line in enumerate(file, start=1):
            if current_line == line_number:
                return line.strip()
    raise ValueError(f"Line {line_number} not found in {file_name}")


def read_line_from_files(file_names, line_number):
    result = {}

    for file_name in file_names:
        result[file_name[:-4]] = read_specific_line(file_name, line_number)
    return result


def write_results_to_file(output_file, results):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)


files = [
    "first_name.txt", "last_name.txt", "age.txt",
    "country.txt", "hobbies.txt", "salary.txt",
    "job_title.txt", "email.txt", "projects.txt", "education.txt"
]

line_number = 5000
all_results = []
max_threads = 100

with ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = []

    for i in range(line_number):
        future = executor.submit(read_line_from_files, files, i + 1)
        futures.append(future)

    for future in futures:
        result = future.result()
        all_results.append(result)

write_results_to_file('result.txt', all_results)
