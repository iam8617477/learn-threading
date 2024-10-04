import threading


def main(l):
    for i in l:
        print(i)


t1 = threading.Thread(target=main, args=([1, 2, 3, 4, 5], ))
t2 = threading.Thread(target=main, args=(['a', 'b', 'c', 'd', 'e'], ))
t1.start()
t2.start()
t1.join()
t2.join()
print('Готово!')
