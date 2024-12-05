import threading
import random
import time


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1, 101):
            amount = random.randint(50, 500)
            self.balance += amount
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {amount}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(1, 101):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
                time.sleep(0.001)
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bank = Bank()
thread_deposit = threading.Thread(target=Bank.deposit, args=(bank,))
thread_take = threading.Thread(target=Bank.take, args=(bank,))
thread_deposit.start()
thread_take.start()
thread_deposit.join()
thread_take.join()
print(f'\nИтоговый баланс: {bank.balance}')