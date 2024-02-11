def next_permutation(a, s=0, e=None):
    if e is None:
        e = len(a)
    ret = a[:]
    for i in range(e - 2, s - 1, -1):
        if ret[i] < ret[i + 1]:
            for j in range(e - 1, i, -1):
                if ret[i] < ret[j]:
                    ret[i], ret[j] = ret[j], ret[i]
                    p, q = i + 1, e - 1
                    while p < q:
                        ret[p], ret[q] = ret[q], ret[p]
                        p += 1
                        q -= 1
                    return ret
    return None


def prev_permutation(a, s=0, e=None):
    if e is None:
        e = len(a)
    ret = a[:]
    for i in range(e - 2, s - 1, -1):
        if ret[i] > ret[i + 1]:
            for j in range(e - 1, i, -1):
                if ret[i] > ret[j]:
                    ret[i], ret[j] = ret[j], ret[i]
                    p, q = i + 1, e - 1
                    while p < q:
                        ret[p], ret[q] = ret[q], ret[p]
                        p += 1
                        q -= 1
                    return ret
    return None
