import colorama
from colorama import Fore


class Vehicle:  # тс
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner # владелец
        self.__model = model
        self.__engine_power = engine_power # мощность двигателя
        self.__color = color
        self.change = False

    def get_model(self):
        return Fore.BLUE + f'Модель: {self.__model}'

    def get_horsepower(self):
        return Fore.BLUE + f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        if self.change:
            print(Fore.BLUE + 'Цвет:', Fore.GREEN + self.__color)
        else:
            print(Fore.BLUE + f'Цвет: {self.__color}')

    def print_info(self):
        print(Fore.BLUE + self.get_model())
        print(self.get_horsepower())
        self.get_color()
        if self.change:
            print(Fore.BLUE + 'Владелец:', Fore.GREEN + self.owner)
        else:
            print(Fore.BLUE + 'Владелец:', self.owner)

    def set_color(self, new_color):
        for i in range(len(self._COLOR_VARIANTS)):
            if new_color.lower() == self._COLOR_VARIANTS[i].lower():
                self.__color = new_color
                self.change = True
                break
        else:
            print(Fore.RED + f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
