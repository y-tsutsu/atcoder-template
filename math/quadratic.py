from fractions import Fraction
from math import isqrt, sqrt

TWO_ROOTS = 'two_roots'
ONE_ROOT = 'one_root'
NO_REAL_ROOTS = 'no_real_roots'
INFINITE_SOLUTIONS = 'infinite_solutions'


def quadratic(a, b, c):
    '''整数係数の方程式ax² + bx + c = 0の状態と実数解を返す

    戻り値は(status, roots)。rootsは昇順のtupleで、厳密に表せる解は
    Fraction、無理数解はfloatになる。恒等式0 = 0の場合のみrootsはNone。
    '''
    if a == 0:
        if b != 0:
            return ONE_ROOT, (Fraction(-c, b),)
        if c == 0:
            return INFINITE_SOLUTIONS, None
        return NO_REAL_ROOTS, ()

    d = b * b - 4 * a * c
    if d < 0:
        return NO_REAL_ROOTS, ()
    if d == 0:
        return ONE_ROOT, (Fraction(-b, 2 * a),)

    r = isqrt(d)
    if r * r == d:
        roots = Fraction(-b - r, 2 * a), Fraction(-b + r, 2 * a)
    else:
        r = sqrt(d)
        roots = (-b - r) / (2 * a), (-b + r) / (2 * a)
    return TWO_ROOTS, tuple(sorted(roots))


def quadratic_integer_roots(a, b, c):
    '''方程式ax² + bx + c = 0の整数解だけを昇順tupleで返す'''
    status, roots = quadratic(a, b, c)
    if status == INFINITE_SOLUTIONS:
        return None
    return tuple(
        x.numerator
        for x in roots
        if isinstance(x, Fraction) and x.denominator == 1
    )


def example():
    # x² - 5x + 6 = 0 は異なる2実根x=2, 3を持つ
    status, roots = quadratic(1, -5, 6)
    print(status, roots)                 # two_roots (2, 3)

    # 2x² + 4x + 2 = 0 は重解x=-1を持つ
    status, roots = quadratic(2, 4, 2)
    print(status, roots)                 # one_root (-1,)

    # x² - 2 = 0 のような無理数解はfloatで返す
    status, roots = quadratic(1, 0, -2)
    print(status, roots)                 # two_roots (-1.414..., 1.414...)

    # x² + 1 = 0 は実数解を持たない
    status, roots = quadratic(1, 0, 1)
    print(status, roots)                 # no_real_roots ()

    # a=0なら一次方程式として解く: 2x - 1 = 0
    status, roots = quadratic(0, 2, -1)
    print(status, roots)                 # one_root (1/2,)

    # 0x² + 0x + 0 = 0 はすべての実数が解
    status, roots = quadratic(0, 0, 0)
    print(status, roots)                 # infinite_solutions None

    # 整数解だけが必要なら専用関数で取得できる
    print(quadratic_integer_roots(1, -5, 6))  # (2, 3)
    print(quadratic_integer_roots(2, 1, -1))  # (-1,): 1/2は除外
    print(quadratic_integer_roots(1, 0, -2))  # (): 無理数解のみ


if __name__ == '__main__':
    example()
