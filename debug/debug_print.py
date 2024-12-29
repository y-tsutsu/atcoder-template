from ast import Call, parse, unparse, walk
from inspect import currentframe, getsourcelines


def dprint(*args, pretty=True):
    def _inner(v):
        def _format_3d(v): return '\n' + '\n'.join(['\n'.join([' '.join([str(z) for z in y]) for y in x]) + '\n' for x in v]).rstrip('\n')
        def _format_2d(v): return '\n' + '\n'.join([' '.join([str(y) for y in x]) for x in v])
        def _dim(v): return (1 + min(_dim(x) for x in v) if v else 1) if isinstance(v, (list, tuple)) else 1 if isinstance(v, str) else 0
        dim = _dim(v) if pretty else -1
        return _format_3d(v) if dim == 3 else _format_2d(v) if dim == 2 else str(v)
    frame = currentframe().f_back
    source_lines, start_line = getsourcelines(frame)
    tree = parse(source_lines[frame.f_lineno - max(1, start_line)].strip())
    call_node = next(node for node in walk(tree) if isinstance(node, Call) and node.func.id == 'dprint')
    arg_names = [unparse(arg) for arg in call_node.args]
    print(', '.join([f'\033[4;35m{name}:\033[0m {_inner(value)}' for name, value in zip(arg_names, args)]))


def example():
    a, b, c = 42, True, 'foo'
    dprint(a, b, c)
    p = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 20, 30], [40, 50, 60], [70, 80, 90]]]
    dprint(p)
    q = [('one', 1), ('two', 2), ('three', 3)]
    dprint(q)
    dprint(q, pretty=False)
    s = ['..#', '#.#', '.#.']
    dprint(s)


if __name__ == '__main__':
    example()
