from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        k = 100
        i = 0
        while k > 0:
            i += 1
            if k > self.power:
                k -= self.power
            else:
                k = 0
            sleep(1)
            print(f'{self.name} сражается {i} дней, осталось {k} воинов.' + '\n', end='')
        print(f"{self.name} одержал победу спустя {i} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
