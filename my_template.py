#!/usr/bin/env python3
from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 9)

try:
    import pypyjit  # type: ignore
    pypyjit.set_param('max_unroll_recursion=-1')
except Exception:
    pass

_tokens = (y for x in stdin for y in x.split())
def read(): return next(_tokens)
def iread(): return int(next(_tokens))


def main():
    pass


if __name__ == '__main__':
    main()
