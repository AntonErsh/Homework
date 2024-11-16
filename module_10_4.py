import os
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

    def guest_arrival(self, *guests: list[Guest]):
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
        guest_at_table = self.tables[i].guest
        number_of_table = self.tables[i].number
        while not self.queue.empty() or guest_at_table:
            if guest_at_table and not guest_at_table.is_alive():
                print(f'{guest_at_table.name} покушал(а) и ушел(ушла).')
                print(f'Стол номер {number_of_table} свободен ')
                guest_at_table = None
            if not self.queue.empty() and guest_at_table is None:
                guest_at_table = self.queue.get(timeout=1)
                print(f'Гость {guest_at_table.name} вышел из очереди и сел за стол номер {number_of_table} ')
                guest_at_table.start()
            i += 1
            if i == len(self.tables):
                i = 0


list_tables = [Table(number) for number in range(1, 3)]
name_guests = ['Vasya', 'Petya', 'Masha', 'Misha', 'Ivan', 'Kaban', 'Rulon Oboev', 'Master']
list_guests = [Guest(name) for name in name_guests]
cafe = Cafe(*list_tables)
cafe.guest_arrival(*list_guests)
cafe.discuss_guests()
