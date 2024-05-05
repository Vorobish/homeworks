#2
immutable_var = 'a', 'b', 'c', 45, False, 0, ['apple', 'coconut']
# список тоже включила, так как это же абстрактный тип данных...
print('Immutable tuple:', immutable_var)
#3
#immutable_var[0] = 'e' #значения str не изменяемые
#immutable_var[3] = 17 #значения int не изменяемые
#immutable_var[4] = True #значения bool не изменяемые
#immutable_var[6] = [2, 2] #список сразу целиком изменить нельзя
immutable_var[6][0] = 'banana' #а элемент в списке изменить - можно
#4
mutable_list = ['a', 'b', 'c', 45, False, 0, ['apple', 'coconut']]
mutable_list[0] = 'e6'
mutable_list[3] = 100
mutable_list[4] = ['banana','peach']
mutable_list[4][1] = 'nuts'
mutable_list[6] = True

print('Mutable list:', mutable_list)


