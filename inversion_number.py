class BIT:
    pass


def compress(a):
    pass


def inv_num(a):
    '''転倒数'''
    p = compress(a)
    tot = 0
    bit = BIT(max(p) + 1)
    for i, v in enumerate(a):
        tot += i - bit.sum(0, v + 1)
        bit.add(v, 1)
    return tot
