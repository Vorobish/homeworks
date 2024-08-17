# устанавливаем 2 библиотеки

# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.

# устанавливаем с помощью pip install

import pandas as pd # для работы с таблицами
import numpy as np
import openpyxl # для загрузки из excel

# смотрим первую pandas
# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.

shop = pd.read_excel('shop.xlsx', 'Sheet1')
print('shop\n', shop)
print('shop.describe()\n', shop.describe())  # все основные агрегированные аналитики
print('shop.T\n', shop.T)   # транспонировка данных (перевернул таблицу)
print('shop.sort_values(by=Price)\n', shop.sort_values(by='Price')) # сортировка
print('shop.dtypes\n', shop.dtypes)  # типы полей
print('shop.head()\n', shop.head())  # просто отображение, как обычный принт
print('shop.tail(2)\n', shop.tail(2)) # вывели только 2 строки
print('shop.index\n', shop.index)   # первый столбец - индекс, начало, конец, шаг
print('shop.loc[1, [Price]]\n', shop.loc[1, ['Price']])   # вывод цены товара с индексом 1
print('shop[shop[Price] > 90]\n', shop[shop['Price'] > 90]) # условие отбора
print('shop\n', shop)
shop.loc[1, 'Price'] = 200  # обновили поле
print('shop\n', shop)
print('sum(shop[Price])\n', sum(shop['Price']))   # сумма итого Price

# смотрим вторую numpy
# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.

mass = np.array(shop.T[1:4])
print('mass\n', mass)
print('mass.ndim\n', mass.ndim)  # 2 оси
print('np.sort(mass)\n', np.sort(mass))  # сортировка каждого списка
print('np.argsort(mass[0])\n', np.argsort(mass[0]))    #индексы соответствуют значениям по возрастанию
print('np.concatenate(mass[0:2])\n', np.concatenate(mass[0:2]))  # соединили два элемента
print('mass.size\n', mass.size)  # размер 15 (15 чисел)
print('mass.shape\n', mass.shape) # размер подробнее 3 строки по 5 чисел
mass2 = mass.reshape(5, 3)  # создал другой массив из этих же элементов, по порядку, но другой размерности
print('mass2\n', mass2)
print('mass[mass > 20]\n', mass[mass > 20]) # вывод только тех чисел, которые больше 20 по порядку
print('sum(mass)\n', sum(mass))    # сумма по столбцам
print('sum(sum(mass))\n', sum(sum(mass)))   # сумма всего
print('mass.sum()\n', mass.sum())
print('mass % 5 == 0\n', mass % 5 == 0)    # логическое значение в каждой ячейке по заданному условию
mass3 = mass * 10   # массовое преобразование
# print(mass3)
# print(mass)
print('mass3 + mass\n', mass3 + mass) # сложили два массива
print('mass.min()\n', mass.min())
