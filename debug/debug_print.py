from ast import Call, parse, unparse, walk
from inspect import currentframe, getsourcelines


def dprint(*args):
    frame = currentframe().f_back
    source_lines, start_line = getsourcelines(frame)
    tree = parse(source_lines[frame.f_lineno - max(1, start_line)].strip())
    call_node = next(node for node in walk(tree) if isinstance(node, Call) and node.func.id == 'dprint')
    arg_names = [unparse(arg) for arg in call_node.args]
    print(', '.join([f'{name} = {value}' for name, value in zip(arg_names, args)]))
