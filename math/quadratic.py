from math import sqrt


def quadratic(a, b, c):
    '''ax^2 + bx + c = 0'''
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        u = -b / (2 * a)
        return int(u) if u.is_integer() else u
    else:
        sd = sqrt(d)
        if sd.is_integer():
            sd = int(sd)
        u = (-b + sd) / (2 * a)
        v = (-b - sd) / (2 * a)
        return int(u) if u.is_integer() else u, int(v) if v.is_integer() else v
