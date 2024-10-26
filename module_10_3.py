import random
import threading
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self) -> None:
        for _ in range(100):
            random_money = random.randint(50, 500)
            self.balance += random_money
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {random_money}. Баланс: {self.balance} ')
            time.sleep(0.001)

    def take(self) -> None:
        for _ in range(100):
            random_money = random.randint(50, 500)
            print(f'Запрос на {random_money} ')
            if self.balance >= 500:
                self.balance -= random_money
                print(f'Снятие: {random_money}. Баланс: {self.balance} ')
            else:
                print(f'Запрос отклонён, недостаточно средств. ')
                self.lock.acquire()
            time.sleep(0.001)


bank1 = Bank()
thread1 = threading.Thread(target=Bank.deposit, args=(bank1, ))
thread2 = threading.Thread(target=Bank.take, args=(bank1, ))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f'Итоговый баланс: {bank1.balance}')
