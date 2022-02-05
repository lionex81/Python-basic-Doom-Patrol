
#1  return function result multiplied by two
def double_result(func):

    def inner(a, b):
        return func(a, b) * 2
    return inner

@double_result
def add(a, b):
    return a + b

print(add(5, 5))
print('__________________')

#2 only odd parameters
def only_odd_parameters(func):
    def inner(*args):
        for i in args:
            if i % 2 == 0:
                print('Pleasure use only odd parameters.')
                break
        else:
            return func(*args)

    return inner

@only_odd_parameters
def add(a, b):
    return a + b
print(add(5, 5))
print(add(5, 4))
print('__________________')

# 3.* logged
from functools import wraps

def logged(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print(f'you called {func.__name__}{args}')
        print(f'it returned {func(*args, **kwargs)}')
    return inner


@logged
def func(*args):
    return 3 + len(args)


print (func.__name__)
print(func(4, 4, 4))


#4
def type_check(correct_type):
    def inner(func):
        def wrapper(*args):
            if type(*args) == correct_type:
                return func(*args)
            else:
                print(f'Wrong Type: {type(func)} should be printed, since non-{correct_type} to decorated function')
        return wrapper
    return inner


@type_check(int)
def times2(num):
    return num * 2

print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function











