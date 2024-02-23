from functools import reduce


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def gcd_multi(*num):
    return reduce(gcd, num)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def lcm_multi(*nums):
    return reduce(lcm, nums)
