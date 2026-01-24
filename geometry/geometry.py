from functools import total_ordering
from math import cos, gcd, sin


def is_collinear(p1, p2, p3):
    return 0 == (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def calc_triangle_area(p1, p2, p3):
    return abs((p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])) / 2


def calc_triangle_area_origin(p1, p2):
    return abs(p1[0] * p2[1] - p1[1] * p2[0]) / 2


def rotate_origin(x, y, radian):
    return x * cos(radian) - y * sin(radian), x * sin(radian) + y * cos(radian)


def rotate(x, y, cx, cy, radian):
    return tuple(a + b for a, b in zip(rotate_origin(x - cx, y - cy, radian), (cx, cy)))


class Sfol:
    '''Standard Form of a Line (ax + by = c)'''

    def __init__(self, x1, y1, x2, y2):
        self.a = y1 - y2
        self.b = x2 - x1
        if self.a == 0:    # 垂直
            self.b = 1
        elif self.b == 0:  # 水平
            self.a = 1
        else:
            g = gcd(self.b, self.a)
            self.b //= g
            self.a //= g
            if self.a < 0:
                self.a *= -1
                self.b *= -1
        self.c = self.a * x1 + self.b * y1

    def __eq__(self, other):
        if not isinstance(other, Sfol):
            return False
        return (self.b, self.a, self.c) == (other.b, other.a, other.c)

    def __hash__(self):
        return hash((self.b, self.a, self.c))

    def __str__(self):
        return f'{self.a} {self.b} {self.c}'


@total_ordering
class SortableVec:
    def __init__(self, x, y):
        assert x != 0 or y != 0
        self.x = x
        self.y = y

    def __lt__(self, other):
        q0, q1 = self.get_quadrant(), other.get_quadrant()
        if q0 != q1:
            return q0 < q1
        return self.cross(other) > 0

    def __eq__(self, other):
        q0, q1 = self.get_quadrant(), other.get_quadrant()
        if q0 != q1:
            return False
        return True if self.cross(other) == 0 else False

    def __str__(self):
        return f'({self.x}, {self.y})'

    def get_quadrant(self):
        if self.y > 0 or (self.y == 0 and self.x > 0):
            return 0
        return 1

    def cross(self, other):
        return self.x * other.y - self.y * other.x


class Vec:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def cross(self, other):
        '''外積'''
        return self.x * other.y - self.y * other.x

    def ccw(self, other):
        '''1:反時計回り, -1:時計回り, 0:直線上'''
        s = self.cross(other)
        return 1 if s > 0 else (-1 if s < 0 else 0)

    def dot(self, other):
        '''内積'''
        return self.x * other.x + self.y * other.y


def calc_distance(px, py, ax, ay, bx, by):
    '''点Pと線分ABとの距離'''
    ap = Vec(px - ax, py - ay)
    ab = Vec(bx - ax, by - ay)
    bp = Vec(px - bx, py - by)
    ba = Vec(ax - bx, ay - by)
    if ap.dot(ab) < 0:
        # 線分PAが最短距離
        return ((px - ax) ** 2 + (py - ay) ** 2) ** 0.5
    elif bp.dot(ba) < 0:
        # 線分PBが最短距離
        return ((px - bx) ** 2 + (py - by) ** 2) ** 0.5
    else:
        # 点Pから線分ABへの垂線が最短距離
        sfol = Sfol(ax, ay, bx, by)
        if sfol.a == 0:
            return abs(px - ax)
        elif sfol.b == 0:
            return abs(py - ay)
        else:
            u = abs(sfol.a * px + sfol.b * py - sfol.c)
            v = (sfol.a ** 2 + sfol.b ** 2) ** 0.5
            return u / v


def calc_intersection_point(px, py, ax, ay, bx, by):
    '''点Pから直線ABへの垂線の交点'''
    sfol = Sfol(ax, ay, bx, by)
    a, b, c = sfol.a, sfol.b, -sfol.c
    x = ((b ** 2) * px - a * b * py - a * c) / (a ** 2 + b ** 2)
    y = ((a ** 2) * py - a * b * px - b * c) / (a ** 2 + b ** 2)
    return x, y


def intersect(ax, ay, bx, by, cx, cy, dx, dy):
    '''線分ABと線分CDが交差するか判定'''
    if Sfol(ax, ay, bx, by) == Sfol(cx, cy, dx, dy):
        ax, bx = min(ax, bx), max(ax, bx)
        cx, dx = min(cx, dx), max(cx, dx)
        if max(ax, cx) > min(bx, dx):
            return False
        ay, by = min(ay, by), max(ay, by)
        cy, dy = min(cy, dy), max(cy, dy)
        if max(ay, cy) > min(by, dy):
            return False
        return True
    else:
        ab = Vec(bx - ax, by - ay)
        ac = Vec(cx - ax, cy - ay)
        ad = Vec(dx - ax, dy - ay)
        s = ab.cross(ac)
        t = ab.cross(ad)
        if s * t > 0:
            return False
        cd = Vec(dx - cx, dy - cy)
        ca = Vec(ax - cx, ay - cy)
        cb = Vec(bx - cx, by - cy)
        s = cd.cross(ca)
        t = cd.cross(cb)
        if s * t > 0:
            return False
        return True
