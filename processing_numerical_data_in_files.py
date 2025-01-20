import os
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

lock = Lock()

def process_file(filename, result_filename):
    sum_ = 0
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            sum_ += (number * 3) / 4

    with lock:
        with open(result_filename, 'a') as result_file:
            result_file.write(f"{sum_}\n")


def main():
    input_folder = './data2'
    result_filename = './result.txt'

    if os.path.exists(result_filename):
        os.remove(result_filename)

    with ThreadPoolExecutor(max_workers=100) as executor:
        for filename in os.listdir(input_folder):
            file_path = os.path.join(input_folder, filename)
            if os.path.isfile(file_path):
                executor.submit(process_file, file_path, result_filename)

if __name__ == "__main__":
    main()
