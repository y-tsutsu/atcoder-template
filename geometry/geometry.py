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


class Line:
    '''Standard Form of a Line (ax + by = c)'''

    def __init__(self, x1, y1, x2, y2):
        assert x1 != x2 or y1 != y2
        self.a = y1 - y2
        self.b = x2 - x1
        if self.a == 0:    # 水平
            self.b = 1
        elif self.b == 0:  # 垂直
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
        if not isinstance(other, Line):
            return False
        return (self.b, self.a, self.c) == (other.b, other.a, other.c)

    def __hash__(self):
        return hash((self.b, self.a, self.c))

    def __str__(self):
        return f'{self.a} {self.b} {self.c}'

    def contains(self, x, y):
        '''点(x, y)が直線上にあるか判定'''
        return self.a * x + self.b * y == self.c

    def is_parallel(self, other):
        '''直線otherと平行か判定'''
        return self.a * other.b - self.b * other.a == 0

    def is_perpendicular(self, other):
        '''直線otherと垂直か判定'''
        return self.a * other.a + self.b * other.b == 0

    def intersection(self, other):
        '''直線otherとの交点を返し、平行ならNone、同一直線ならLineを返す'''
        det = self.a * other.b - other.a * self.b
        if det == 0:
            return self if self == other else None
        x = (self.c * other.b - other.c * self.b) / det
        y = (self.a * other.c - other.a * self.c) / det
        return x, y

    def distance(self, x, y):
        '''点(x, y)との距離を返す'''
        u = abs(self.a * x + self.b * y - self.c)
        return u / (self.a ** 2 + self.b ** 2) ** 0.5

    def projection(self, x, y):
        '''点(x, y)から直線へ下ろした垂線の足を返す'''
        d = (self.a * x + self.b * y - self.c) / (self.a ** 2 + self.b ** 2)
        return x - self.a * d, y - self.b * d


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

    def dot(self, other):
        '''内積（符号でなす角が鋭角・直角・鈍角か判定）'''
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        '''外積（符号で回転方向、絶対値で平行四辺形の面積、0で平行を判定）'''
        return self.x * other.y - self.y * other.x

    def ccw(self, other):
        '''1:反時計回り, -1:時計回り, 0:直線上'''
        s = self.cross(other)
        return 1 if s > 0 else (-1 if s < 0 else 0)


def calc_distance(px, py, ax, ay, bx, by):
    '''点Pと線分ABとの距離'''
    if ax == bx and ay == by:
        return ((px - ax) ** 2 + (py - ay) ** 2) ** 0.5
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
        line = Line(ax, ay, bx, by)
        if line.a == 0:
            return abs(py - ay)
        elif line.b == 0:
            return abs(px - ax)
        else:
            return line.distance(px, py)


def calc_intersection_point(px, py, ax, ay, bx, by):
    '''点Pから直線ABへの垂線の交点'''
    return Line(ax, ay, bx, by).projection(px, py)


def intersect(ax, ay, bx, by, cx, cy, dx, dy):
    '''線分ABと線分CDが交差するか判定'''
    def cross(x1, y1, x2, y2, x3, y3):
        return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    s = cross(ax, ay, bx, by, cx, cy)
    t = cross(ax, ay, bx, by, dx, dy)
    u = cross(cx, cy, dx, dy, ax, ay)
    v = cross(cx, cy, dx, dy, bx, by)
    if s == t == u == v == 0:
        return (max(min(ax, bx), min(cx, dx)) <= min(max(ax, bx), max(cx, dx)) and
                max(min(ay, by), min(cy, dy)) <= min(max(ay, by), max(cy, dy)))
    return s * t <= 0 and u * v <= 0
