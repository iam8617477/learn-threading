from concurrent.futures import ThreadPoolExecutor, wait
import time

data = [("asdf", 0.7), ("ghjk", 1.4), ("zxcl", 3.2), ("vbnm", 4.1), ("poiu", 2.7), ("ytre", 0.3), ("wqsx", 1.1)]


def f(args):
    time.sleep(args[1])
    return args[0]


with ThreadPoolExecutor(max_workers=5) as executor:
    fs = [executor.submit(f, (i, k)) for i, k in data]
    done, not_done = wait(fs, timeout=1.5)
    for d in done:
        print(d.result())
