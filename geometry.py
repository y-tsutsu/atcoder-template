from math import gcd


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


class Vec:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'{self.x} {self.y}'

    def cross(self, other):
        '''外積'''
        return self.x * other.y - self.y * other.x

    def ccw(self, other):
        '''1:反時計回り, -1:時計回り, 0:直線上'''
        s = self.cross(other)
        return 1 if s > 0 else (-1 if s < 0 else 0)
