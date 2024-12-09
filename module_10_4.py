import threading
import time
import random
from queue import Queue


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:

    def __init__(self, *tables):
        self.tables = [*tables]
        self.queue = Queue()

    def guest_arrival(self, *guests):
        self.guests = [*guests]
        for guest in self.guests:
            for table in self.tables:
                if not table.guest is None:
                    if all(table.guest is not None for table in self.tables):
                        print(f'{guest.name} в очереди')
                        self.queue.put(guest)
                        break
                if table.guest is None:
                    table.guest = guest.name
                    Guest.start(guest)
                    Guest.join(guest)
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break

    def discuss_guests(self):
        while not self.queue.empty() and all(table.guest is not None for table in self.tables):
            for table in self.tables:
                if not Guest(table.guest).is_alive():
                    print(f'{table.guest} за текущим столом покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        guest = self.queue.get()
                        table.guest = guest.name
                        print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        Guest.start(guest)
                        Guest.join(guest)


tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
