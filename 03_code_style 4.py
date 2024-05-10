# -*- coding: utf-8 -*-

# блоки кода

x, y = 10, 29

if x < 0:
    print('Х меньше нуля')
    z = x ** 2 + y
else:
    print('Х больше нуля')
    z = x - y
print('Результат', z)

# вложенные блоки кода

name = input('Enter your name >>>')
if name in ('Ola', 'Sofi', 'Katy'):
    opponent = name
else:
    opponent = 'anonymous'
print('Hi,', opponent)

# оператор pass

if x < 0:
    if y > 0:
        z = -x + y
    else:
        z = -x - y
else:
    z = x + y

# 4 пробела на каждый уровень отступа

if x < 0:
    if y <= 0:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось, хливкие шорьки пырялись по наве',
           'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын! Он так свирлеп и дик',
           'А в глуше рымит исполин - Злопастный Брандашмыг!']

# пробелы в операторах

x = 2
is_big = x >= 3000

x = my_poem[-1]
print(x)
my_list = [2, 3, 4, 5, 6]

# reformat кода
x, y = 3, 8

if x == 3:
    print(42)

if x < 0:
    if y > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print('стой!')

# названия переменных

count_my_pets = 34
if count_my_pets > 10:
    print('I need more space for my pets!')

my_pets = ['cat', 'wolf', 'ostrich']
if 'lion' in my_pets:
    print('Wow!')

#   i j k - для циклов
#   x y z - для координат

i = 34
j = 43
if i > j:
    print()
k = 9
if k > 0:
    print()
