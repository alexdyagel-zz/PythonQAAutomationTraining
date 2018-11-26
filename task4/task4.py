def arange(*args):
    """
    Like xrange() but better.
    Function requires 1-3 int or long arguments
    and last argument shouldn't be 0.
    Written on python 2.7
    """

    if not all(isinstance(el, (int, long)) for el in args):
        raise TypeError('Arguments must be integer or long')

    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError('arange() requires 1-3 int arguments')

    if step == 0:
        raise ValueError('xrange() arg 3 must not be zero')

    number = start
    if step < 0:
        while number > stop:
            yield number
            number += step
    else:
        while number < stop:
            yield number
            number += step


g = arange(5)
print(list(g))
