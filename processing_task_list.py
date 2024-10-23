import time
from concurrent.futures import ThreadPoolExecutor, wait

timeouts = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]
numbers = [2257, 6217, 6594, 2259, 5284, 3568, 1741, 5462, 7494, 8971, 3157, 3998, 2040, 8828, 8769, 6976, 9367, 1267, 6255, 7322]


def process_number(timeout, number):
    time.sleep(timeout)
    return number


results = list()
with ThreadPoolExecutor(max_workers=len(timeouts)) as executor:
    fs = [executor.submit(process_number, t, numbers[i]) for i, t in enumerate(timeouts)]
    done, not_done = wait(fs, timeout=3)
    for f in done:
        results.append(f.result())

print(sum(results))
