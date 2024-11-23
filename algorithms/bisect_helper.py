from bisect import bisect_left, bisect_right


def lt(a, x):
    i = bisect_left(a, x)
    return None if i == 0 else a[i - 1]


def le(a, x):
    i = bisect_right(a, x)
    return None if i == 0 else a[i - 1]


def gt(a, x):
    i = bisect_right(a, x)
    return None if i == len(a) else a[i]


def ge(a, x):
    i = bisect_left(a, x)
    return None if i == len(a) else a[i]


def lt_count(a, x):
    return bisect_left(a, x)


def le_count(a, x):
    return bisect_right(a, x)


def gt_count(a, x):
    return len(a) - bisect_right(a, x)


def ge_count(a, x):
    return len(a) - bisect_left(a, x)


def range_count(a, lo, hi):
    return bisect_right(a, hi) - bisect_left(a, lo)


def range_inclusive_count(a, lo, hi):
    '''[lo, hi]'''
    return range_count(a, lo, hi)


def range_exclusive_count(a, lo, hi):
    '''[lo, hi)'''
    return bisect_left(a, hi) - bisect_left(a, lo)


def kth_lt(a, x, k):
    i = bisect_left(a, x)
    return None if (i - 1 - k) < 0 else a[i - 1 - k]


def kth_le(a, x, k):
    i = bisect_right(a, x)
    return None if (i - 1 - k) < 0 else a[i - 1 - k]


def kth_gt(a, x, k):
    i = bisect_right(a, x)
    return None if (i + k) >= len(a) else a[i + k]


def kth_ge(a, x, k):
    i = bisect_left(a, x)
    return None if (i + k) >= len(a) else a[i + k]
