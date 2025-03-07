class Range():
    pass


def recurboost(func=None, stack=[]):
    pass


def split_seg(mainrange: Range):
    '''seg_tree的な区間に分割'''
    ret = []

    @recurboost
    def dfs(segrange: Range):
        if segrange.contained_in(mainrange):
            ret.append(segrange)
            yield
        if not mainrange.is_overlaps(segrange):
            yield
        m = (segrange.s + segrange.e) // 2
        yield dfs(Range(segrange.s, m))
        yield dfs(Range(m, segrange.e))
        yield

    e = 1
    while e < mainrange.e:
        e <<= 1
    dfs(Range(0, e))
    return ret
