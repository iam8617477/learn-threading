import os
from multiprocessing import Pool

BASE_DIR = 'output_files_8.4'


def write_from_file(file_name):
    with open(os.path.join(BASE_DIR, file_name)) as file:
        _int = file.read()
        return int(_int.strip('\n'))


if __name__ == '__main__':
    with Pool(4) as p:
        result = p.map(write_from_file, os.listdir(BASE_DIR))
        print(sum(result))
