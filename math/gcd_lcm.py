from functools import reduce
from math import gcd


def my_gcd(*num):
    return reduce(gcd, num)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def my_lcm(*nums):
    return reduce(lcm, nums)
