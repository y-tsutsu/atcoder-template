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
    a = [0 for _ in range(max + 1)]
    for i in range(2, int(max ** 0.5) + 1):
        if a[i] != 0:
            continue
        n = i * 2
        while n <= max:
            a[n] = 1
            n += i
    return [i for i, x in enumerate(a) if i >= 2 and x == 0]
