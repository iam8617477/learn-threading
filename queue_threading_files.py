from queue import Empty, Queue
from threading import Thread

elements = ['file1.txt', 'file2.txt', 'file3.txt']


def count_words_in_files(q, file_paths):
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            print(len(words))
            q.put(len(words))


def count_lines_in_files(q, file_paths):
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(len(lines))
            q.put(len(lines))


def consumer_words(queue):
    l = list()
    while True:
        try:
            item = queue.get(timeout=0.6)
            print('w', item)
            l.append(item)
            queue.task_done()
        except Empty:
            break
    print('rw', sum(l))


def consumer_lines(queue):
    l = list()
    while True:
        try:
            item = queue.get(timeout=0.6)
            l.append(item)
            print('l', item)
            queue.task_done()
        except Empty:
            break
    print('rl', sum(l))


def main():
    queue_words = Queue()
    queue_lines = Queue()
    words_thread = Thread(target=count_words_in_files, args=(queue_words, elements), daemon=True)
    words_thread.start()

    consumer_thread = Thread(target=count_lines_in_files, args=(queue_lines, elements), daemon=True)
    consumer_thread.start()

    consumer_words(queue_words)
    consumer_lines(queue_lines)

    queue_words.join()
    queue_lines.join()


if __name__ == '__main__':
    main()

