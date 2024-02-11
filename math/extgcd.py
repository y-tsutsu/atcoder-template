def extgcd(a, b):
    '''(g, x, y): ax + by = 1
    前提条件: aとbは互いに素である必要がある
    xがaの逆元（mod b）になる（ただしg==1なのが条件 そうでない場合は逆元が存在しない）'''
    if b == 0:
        return a, 1, 0
    g, x, y = extgcd(b, a % b)
    return g, y, x - a // b * y


def solve_linear_indefinite_equation(a, b, c):
    '''(x, y): ax + by = c'''
    g, x, y = extgcd(a, b)
    if c % g != 0:
        return None
    v = c // g
    return x * v, y * v
