from itertools import pairwise
from math import dist, isqrt
from statistics import median, mode, multimode
from sys import set_int_max_str_digits, setrecursionlimit

'''再帰関数の高速化（PyPy）'''
try:
    import pypyjit  # type: ignore
    pypyjit.set_param('max_unroll_recursion=-1')
except Exception:
    pass


'''再帰呼び出しの上限数設定'''
setrecursionlimit(10 ** 9)


'''str->int変換の制限解除'''
set_int_max_str_digits(0)
v = int('1' * 5000)
print(v)


'''powの負の指数'''
print(pow(2, -1))
# 逆元
MOD = 998244353
print(pow(2, -1, MOD))


'''平方根（整数）'''
# 切り捨て
print(isqrt(5))
# 切り上げ（引数がマイナスにならないように注意）
print(isqrt(5 - 1) + 1)


'''平方数の判定'''
def is_square_num(num): return isqrt(num) ** 2 == num
# print(4, is_square_num(4))
# print(5, is_square_num(5))


'''隣り合った要素を列挙'''
a = [i for i in range(10)]
for i, j in pairwise(a):
    print(i, j)


'''最頻値'''
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
print(mode(a))
print(multimode(a))


'''マンハッタン距離の総和を最小化するときは中央値を使う'''
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = int(median(x))
tot = sum([abs(m - v) for v in x])
print(tot)


'''ユークリッド距離'''
d = dist((1, 2), (3, 6))
print(d)


'''2次配列の右回転'''
a = [[1, 2, 3], [4, 5, 6]]
print([x for x in zip(*a[::-1])])


'''2次配列の左回転'''
a = [[1, 2, 3], [4, 5, 6]]
print([x for x in zip(*[y[::-1] for y in a])])
