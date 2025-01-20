import threading
import time
import random


bidder_names = ["Сергей", "Борис", "Виктор", "Евдоким", "Егор"]


auction_start_painting = threading.Event()
auction_start_clock = threading.Event()


def bidder(name, auction_event, item):
    print(f"Участник {name} готов к аукциону за {item}.")
    auction_event.wait()
    print(f"Участник {name} делает ставку на {item}.")


if __name__ == "__main__":
    painting_threads = []
    clock_threads = []

    for name in bidder_names:
        t_painting = threading.Thread(target=bidder, args=(name, auction_start_painting, "редкую картину"))
        t_clock = threading.Thread(target=bidder, args=(name, auction_start_clock, "антикварные часы"))
        painting_threads.append(t_painting)
        clock_threads.append(t_clock)
        t_painting.start()
        t_clock.start()

    print("Аукцион за редкую картину начинается!")
    auction_start_painting.set()
    time.sleep(3)
    print("Аукцион за редкую картину завершился!")
    winner_painting = random.choice(bidder_names)

    print("Аукцион за антикварные часы начинается!")
    auction_start_clock.set()
    time.sleep(3)
    print("Аукцион за антикварные часы завершился!")
    winner_clock = random.choice(bidder_names)

    for t in painting_threads + clock_threads:
        t.join()

    print(f"Победитель аукциона за редкую картину: {winner_painting}")
    print(f"Победитель аукциона за антикварные часы: {winner_clock}")
