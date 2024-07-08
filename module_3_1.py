calls =0

def count_calls():
    global calls
    calls += 1

def string_info(str_):
    count_calls()
    tuple_ = len(str_), str_.upper(), str_.lower()
    return tuple_

def is_contains(str_, list_):
    count_calls()
    if str_ in list_:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)




