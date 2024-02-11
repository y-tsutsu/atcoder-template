def extgcd(a, b):
    '''(g, x, y): ax + by = 1
    前提条件: aとbは互いに素である必要がある
    xがaの逆元（mod b）になる（ただしg==1なのが条件 そうでない場合は逆元が存在しない）'''
    if b == 0:
        return a, 1, 0
    g, x, y = extgcd(b, a % b)
    return g, y, x - a // b * y
