from fractions import Fraction

UNIQUE = 'unique'
NONE = 'none'
INFINITE = 'infinite'


def system_of_equations(a, b, c, d, u, v):
    '''連立方程式ax + by = u, cx + dy = vの解の状態と解を返す

    戻り値は一意解なら(UNIQUE, (x, y))、解なしなら(NONE, None)、
    解が無限に存在するなら(INFINITE, None)。x, yはFractionで正確に表す。
    '''
    if (a == 0 and b == 0 and u != 0) or (c == 0 and d == 0 and v != 0):
        return NONE, None

    det = a * d - b * c
    if det != 0:
        x = Fraction(u * d - b * v, det)
        y = Fraction(a * v - u * c, det)
        return UNIQUE, (x, y)

    if a * v == c * u and b * v == d * u:
        return INFINITE, None
    return NONE, None


def example():
    # x + y = 5, x - y = 1 の一意解はx=3, y=2
    status, solution = system_of_equations(1, 1, 1, -1, 5, 1)
    print(status)                         # unique
    print(*solution)                     # 3 2

    # 2x + 4y = 1, x - y = 0 のような分数解も誤差なく返す
    status, solution = system_of_equations(2, 4, 1, -1, 1, 0)
    print(status)                         # unique
    print(*solution)                     # 1/6 1/6

    # 左辺が同じなのに右辺が異なるため解なし
    status, solution = system_of_equations(1, 2, 2, 4, 3, 7)
    print(status, solution)               # none None

    # 2本の式が同じ直線を表すため解は無限に存在
    status, solution = system_of_equations(1, 2, 2, 4, 3, 6)
    print(status, solution)               # infinite None


if __name__ == '__main__':
    example()
