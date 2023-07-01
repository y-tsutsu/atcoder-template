from functools import cmp_to_key


def cmp(u, v):
    '''u: a / b, v: c / d'''
    a, b = u
    c, d = v
    if a * d < c * b:
        return -1
    if a * d > c * b:
        return 1
    else:
        return 0


a = [(1, 2), (1, 3), (2, 3), (3, 4), (3, 5)]
a.sort(key=cmp_to_key(cmp))
print(a)
