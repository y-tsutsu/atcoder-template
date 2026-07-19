from math import isqrt


def prime_factorize(n):
    assert n > 0
    ret = []
    while n % 2 == 0:
        ret.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            ret.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        ret.append(n)
    return ret


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes(n):
    a = [0 for _ in range(n + 1)]
    for i in range(2, isqrt(n) + 1):
        if a[i] != 0:
            continue
        p = i * 2
        while p <= n:
            a[p] = 1
            p += i
    return [i for i, x in enumerate(a) if i >= 2 and x == 0]


class PrimeFactorizer:
    '''最小素因数を前計算し、多数の整数を高速に素因数分解する'''

    def __init__(self, n):
        self.n = n
        self.spf = [0 for _ in range(n + 1)]
        for p in range(2, isqrt(n) + 1):
            if self.spf[p] != 0:
                continue
            for x in range(p * p, n + 1, p):
                if self.spf[x] == 0:
                    self.spf[x] = p

    def factorize(self, n):
        '''素因数を重複を含む昇順のリストで返す'''
        assert 0 < n <= self.n
        ret = []
        while n > 1:
            p = self.spf[n]
            if p == 0:
                p = n
            ret.append(p)
            n //= p
        return ret

    def factorize_count(self, n):
        '''素因数と指数を辞書で返す'''
        ret = {}
        for p in self.factorize(n):
            ret[p] = ret.get(p, 0) + 1
        return ret


def example():
    a = [12, 25, 42, 97]
    factorizer = PrimeFactorizer(max(a))
    for x in a:
        print(factorizer.factorize(x))
        print(factorizer.factorize_count(x))


if __name__ == '__main__':
    example()
