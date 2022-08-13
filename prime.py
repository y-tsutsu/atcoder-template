def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes(max):
    ret = [2]
    a = [1 for _ in range(max + 1)]
    for i in range(3, max + 1, 2):
        n = i
        if a[n] == 1:
            ret.append(n)
        while n <= max:
            a[n] += 1
            n += i
    return ret
