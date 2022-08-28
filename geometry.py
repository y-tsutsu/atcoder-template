class Vec:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def cross(self, other):
        '''外積'''
        return self.x * other.y - self.y * other.x

    def ccw(self, other):
        '''1:反時計回り, -1:時計回り, 0:直線上'''
        s = self.cross(other)
        return 1 if s > 0 else (-1 if s < 0 else 0)
