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
        waitimg = [] # временный список ожидания (для проверки)
        for guest in self.guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest.name
                    # self.guests.pop(0)
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
                else:
                    continue


        print(self.guests)
        #     waitimg.append(guest.name)
        #     print(f'{guest.name} в очереди')
        # print(waitimg)



    #     self.queue.put(guest.name)
    #     guest_ = Guest(self.guests)
    #     guest_.start()
    #     guest_.join()
    #     print(f'{guest.name} сел(-а) за стол номер {table.number}')



tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
