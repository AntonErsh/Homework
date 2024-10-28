import random
import threading
import time
from queue import Queue


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        i = 0
        for guest in guests:
            if i < len(self.tables) and self.tables[i].guest is None:
                self.tables[i].guest = guest
                print(f'{guest.name} сел(-а) за стол номер {self.tables[i].number} ')
                guest.start()
                i += 1
            else:
                self.queue.put(guest)
                print(f'Гость {guest.name} в очереди ')

    def discuss_guests(self):
        i = 0
        while not self.queue.empty() or self.tables[i].guest:
            if self.tables[i].guest and not self.tables[i].guest.is_alive():
                print(f'{self.tables[i].guest.name} покушал(а) и ушел(ушла).'
                      f' \n Стол номер {self.tables[i].number} свободен ')
                self.tables[i].guest = None
            if not self.queue.empty() and self.tables[i].guest is None:
                self.tables[i].guest = self.queue.get(timeout=1)
                print(f'Гость {self.tables[i].guest.name} вышел из очереди'
                      f' и сел за стол номер {self.tables[i].number} ')
                self.tables[i].guest.start()
            i += 1
            if i == len(self.tables):
                i = 0
            if self.tables[i].guest and self.queue.empty():
                self.tables[i].guest.join()


list_tables = [Table(number) for number in range(1, 6)]
name_guests = ['Vasya', 'Petya', 'Masha', 'Misha', 'Ivan', 'Kaban', 'Rulon Oboev', 'Master']
list_guests = [Guest(name) for name in name_guests]
cafe = Cafe(*list_tables)
cafe.guest_arrival(*list_guests)
cafe.discuss_guests()
