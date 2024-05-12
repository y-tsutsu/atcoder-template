from inspect import currentframe


def dprint(*args):
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args))
