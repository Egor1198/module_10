import time
import random
import threading


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            operation = random.randint(50,500)
            with self.lock:
                self.balance += operation
                print(f'Пополнение: {operation}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            operation = random.randint(50, 500)
            print(f'Запрос на случайное число')
            with self.lock:
                if operation <= self.balance:
                    self.balance -= operation
                    print(f'Снятие: {operation}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонен, недостаточно средств')
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

