import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy = 100
        day_count = 0
        print(f'{self.name}, на нас напали! ')
        while enemy > 0:
            enemy -= self.power
            time.sleep(1)
            day_count += 1
            if enemy > 0:
                print(f'{self.name} сражается {day_count} дней, осталось врагов {enemy} ')
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)! ')


first_knight = Knight('Король Артур', 9)
second_knight = Knight('Shrek', 51)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
