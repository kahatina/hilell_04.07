def pow(x):
    return x ** 2

def some_gen(begin: int, end: int, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """

    first_number = begin

    yield begin

    for n in range(end - 1):
        next_number = func(first_number)
        first_number = next_number
        yield next_number

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')