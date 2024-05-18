print('Функция с параметрами по умолчанию:')
print()

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2, 3)
print_params(1, 2, c=5)
print_params(c=5, a='для примера', b='в разнобой')
print_params(b=25)
print_params(c=[1, 2, 3])

print()
print('Распаковка параметров:')
print()

values_list = [False, 'Hi!', 155.7]
values_dict = {'a': 2050, 'b': 'пока', 'c': True}

print_params(*values_list)
print_params(**values_dict)

print()
print('Распаковка + отдельные параметры:')
print()

values_list_2 = ['ку-ку', 789]
print_params(*values_list_2, 42)




