import threading
import time


class Knight(threading.Thread):
    # Конструктор класса
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0  # Количество дней сражения

    # Метод для сражения
    def run(self):
        print(f"{self.name}, на нас напали!")
        while enemies_left > 0:
            time.sleep(1)  # Задержка на 1 секунду
            self.days += 1
            # Снижение числа врагов, синхронизированное с другими потоками
            with threading.Lock():  # Гарантия атомарности операции
                if enemies_left > 0:
                    enemies_left -= self.power
                    enemies_left = max(enemies_left, 0)  # Чтобы число врагов не стало отрицательным
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {enemies_left} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Глобальная переменная для отслеживания общего числа врагов
enemies_left = 100

# Создание объектов-рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения всех потоков
first_knight.join()
second_knight.join()

# Завершающее сообщение
print("Все битвы закончились!")
