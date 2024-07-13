def apply_all_func(int_list, *function):
    res = {}
    for f in function:
        res.update({f.__name__: f(int_list)})
    return res


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
