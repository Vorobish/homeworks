def all_variants(text):
    n = 1   # кол-во букв
    while n <= len(text):
        j = 0   # итератор
        while j + n <= len(text):
            yield text[j:j+n]
            j += 1
        if n >= len(text):
            break
        n += 1


a = all_variants("abc")
for i in a:
    print(i)