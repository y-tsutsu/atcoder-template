class SortedSet:
    pass


def inv_num(a):
    '''転倒数'''
    tot = 0
    ss = SortedSet()
    for v in a:
        i = ss.index_right(v)
        tot += len(ss) - i
        ss.add(v)
    return tot
