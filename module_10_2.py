import threading
import  time


class Knight(threading.Thread):
    
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.day_counter = 0

    def timer(self):
        time.sleep(1)
        self.day_counter += 1

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.timer()
            self.enemies -= self.power
            print(f'{self.name} сражается {self.day_counter} дней(день)..., осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {self.day_counter} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
