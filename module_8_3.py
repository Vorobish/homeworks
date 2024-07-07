class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message


class Car:
    cars = list([])

    def __init__(self, model, vin, number):  # vin номер автомобиля (целое число). Уровень доступа private.
        self.model = model
        self.__vin_number = vin
        self.__is_valid_vin()
        self.__number = number
        self.__is_valid_numbers()
        if self.has_already():
            Car.cars.append(self)


    def __is_valid_vin(self):
        if not isinstance(self.__vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= int(self.__vin_number) <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __eq__(self, other):
        return self.model == other.model and self.__number == other.__number and self.__vin_number == other.__vin_number

    def has_already(self):
        for i in Car.cars:
            if self == i:
                # print(f'Модель {self.model} с номерами: {self.__vin_number}, {self.__number} - уже существует')
                return False
        else:
            return True

    def __is_valid_numbers(self):
        if not isinstance(self.__number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(self.__number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        if not self.has_already(): # засунула сюда, чтобы по Вашим проверочным скриптам отрабатывало
            raise IncorrectCarNumbers('Модель с такими атрибутами уже существует')
        else:
            return True

    def __str__(self):
        return f'Модель: {self.model}, ВИН номер: {self.__vin_number}, Номер машины: {self.__number}\n'

# 1

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

# 2

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

# 3

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

# print(*Car.cars)

# 4

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

# 5

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

print(*Car.cars)
