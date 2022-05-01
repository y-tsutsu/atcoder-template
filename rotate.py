from math import cos, sin


def rotate_origin(x, y, radian):
    return x * cos(radian) - y * sin(radian), x * sin(radian) + y * cos(radian)


def rotate(x, y, cx, cy, radian):
    return tuple(a + b for a, b in zip(rotate_origin(x - cx, y - cy, radian), (cx, cy)))
