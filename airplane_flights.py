import threading
import time


aircrafts = {
    'Boeing 737': 6,
    'Airbus A320': 9,
    'Boeing 747': 6,
    'Airbus A380': 7,
}


def flight_simulation(model, flight_time):
    print(f"{model} начал полет. Время полета: {flight_time} сек.")
    time.sleep(flight_time)
    print(f"{model} завершил полет.")


def main():
    for model, flight_time in aircrafts.items():
        thread = threading.Thread(target=flight_simulation, args=(model, flight_time, ))
        thread.start()
    time.sleep(5)
    print(f"Количество самолетов в воздухе после 5 секунд: {threading.active_count()-1}")


main()
