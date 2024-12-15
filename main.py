#!/usr/bin/env python3
from ast import Call, parse, unparse, walk
from inspect import currentframe, getsourcelines
from sys import stdin

_tokens = (y for x in stdin for y in x.split())
def read(): return next(_tokens)
def iread(): return int(next(_tokens))


def dprint(*args):
    def _inner(value):
        type0, type1 = (list, tuple), (list, tuple, str)
        if isinstance(value, type0) and value and isinstance(value[0], type0) and value[0] and isinstance(value[0][0], type1):
            return '\n' + '\n'.join(['\n'.join([' '.join([str(z) for z in y]) for y in x]) + '\n' for x in value]).rstrip('\n')
        if isinstance(value, type0) and value and isinstance(value[0], type1):
            return '\n' + '\n'.join([' '.join([str(y) for y in x]) for x in value])
        return str(value)
    frame = currentframe().f_back
    source_lines, start_line = getsourcelines(frame)
    tree = parse(source_lines[frame.f_lineno - max(1, start_line)].strip())
    call_node = next(node for node in walk(tree) if isinstance(node, Call) and node.func.id == 'dprint')
    arg_names = [unparse(arg) for arg in call_node.args]
    print(', '.join([f'\033[4;35m{name}:\033[0m {_inner(value)}' for name, value in zip(arg_names, args)]))


def main():
    pass


if __name__ == '__main__':
    main()
