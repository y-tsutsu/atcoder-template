from itertools import accumulate


def acm2dim(p):
    q = [list(accumulate(x, initial=0)) for x in p]
    q = [x for x in zip(*q)]
    q = [list(accumulate(x, initial=0)) for x in q]
    return [list(x) for x in zip(*q)]
