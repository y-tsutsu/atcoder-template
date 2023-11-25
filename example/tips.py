from itertools import pairwise
from math import dist, isqrt
from statistics import mode, multimode
from sys import set_int_max_str_digits

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


'''ユークリッド距離'''
d = dist((1, 2), (3, 6))
print(d)