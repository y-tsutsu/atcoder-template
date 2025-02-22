def divisors(n):
    ld, ud = [], []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ld.append(i)
            if i == n // i:
                continue
            ud.append(n // i)
    return ld + ud[::-1]


def divisors_table(n):
    ret = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            ret[j].append(i)
    return ret


def divisors_counts(n):
    ret = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            ret[j] += 1
    return ret
