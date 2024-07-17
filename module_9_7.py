def is_prime(func):
    def wraper(*args):
        result = func(*args)
        for j in args:
            if not isinstance(j, int):
                return result
        for i in range(2, result):
            if result % i == 0:
                print("Составное")
                break
        else:
            if result <= 0:
                print('сумма должна быть больше 0')
            else:
                print("Простое")
        return result
    return wraper


@is_prime
def sum_three(a, b, c):
    if isinstance(a, int) is False or isinstance(b, int) is False or isinstance(c, int) is False:
        return 'все аргументы д/б числами'
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
