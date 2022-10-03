def multiply_func(*args):
    value = 1
    for i in args:
        value *= i
    print(value)
    return value