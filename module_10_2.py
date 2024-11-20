import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int, wariors: int = 100):
        super().__init__()
        self.name = name
        self.power = power
        self.wariors = wariors

    def run(self):
        print(f'{self.name}, на нас напали!')
        day_num = 0
        while self.wariors > 0:
            time.sleep(1)
            day_num += 1
            self.wariors -= self.power
            print(f'{self.name} сражается {day_num} день(дня)..., осталось {self.wariors} воинов.')
        print(f'{self.name} одержал победу спустя {day_num} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')