print('#1')

def params(*params):
    print(*params)


params(4, 'hi', True)

print('#2')

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


