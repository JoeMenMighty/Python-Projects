def add(*args):
    sum_ = 0
    for arg in args:
        sum_ += arg
    return sum_


print(add(1, 2, 3, 4, 5))


def calculate(first, **kwargs):
    answer = 0
    div = kwargs.get('div')
    mult = kwargs.get('multiply')
    add = kwargs.get('add')
    sub = kwargs.get('sub')

    for key, val in kwargs.items():
        if key == 'multiply':
            pass


calculate(2, add=3, multiply=4, sub=2, div=3)
