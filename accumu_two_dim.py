from itertools import accumulate


def acm2dim(p):
    q = [[0] + list(accumulate(x)) for x in p]
    q = [x for x in zip(*q)]
    q = [[0] + list(accumulate(x)) for x in q]
    return [list(x) for x in zip(*q)]
