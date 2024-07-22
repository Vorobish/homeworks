def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)):
            if j+i+1 <= len(text):
                yield text[j:j+i+1]
            else:
                break


a = all_variants("abc")
for i in a:
    print(i)
