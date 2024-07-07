def personal_sum(numbers):
    try:
        len_ = len(numbers)
        result = 0
        incorrect_data = 0
        for i in numbers:
            try:
                result += i
            except TypeError as exc:
                incorrect_data += 1
                print('Некорректный тип данных для подсчёта суммы -', i)
        return result, incorrect_data
    except:
        print('В numbers записан некорректный тип данных')


def calculate_average(numbers):
    personal_sum_n = personal_sum(numbers)
    if personal_sum_n:
        avg = 0
        try:
            summ = personal_sum_n[0]
            count_int = len(numbers) - personal_sum_n[1]
            return summ / count_int
        except ZeroDivisionError as exc:
            return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
