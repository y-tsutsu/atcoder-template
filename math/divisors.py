def divisors(n):
    ld, ud = [], []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ld.append(i)
            if i == n // i:
                continue
            ud.append(n // i)
    return ld + ud[::-1]


def div_counts(n):
    ret = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        p = i
        while p <= n:
            ret[p] += 1
            p += i
    return ret
