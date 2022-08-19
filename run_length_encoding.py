from itertools import groupby


def rle(x):
    return [(a, len(list(b))) for a, b in groupby(x)]
