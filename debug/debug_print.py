from ast import Call, parse, unparse, walk
from inspect import currentframe, getsourcelines


def dprint(*args):
    def _inner(value):
        type0, type1 = (list, tuple), (list, tuple, str)
        if isinstance(value, type0) and isinstance(value[0], type0) and isinstance(value[0][0], type1):
            return '\n' + '\n'.join(['\n'.join([' '.join([str(z) for z in y]) for y in x]) + '\n' for x in value]).rstrip('\n')
        if isinstance(value, type0) and isinstance(value[0], type1):
            return '\n' + '\n'.join([' '.join([str(y) for y in x]) for x in value])
        return str(value)
    frame = currentframe().f_back
    source_lines, start_line = getsourcelines(frame)
    tree = parse(source_lines[frame.f_lineno - max(1, start_line)].strip())
    call_node = next(node for node in walk(tree) if isinstance(node, Call) and node.func.id == 'dprint')
    arg_names = [unparse(arg) for arg in call_node.args]
    print(', '.join([f'\033[4;35m{name}:\033[0m {_inner(value)}' for name, value in zip(arg_names, args)]))
