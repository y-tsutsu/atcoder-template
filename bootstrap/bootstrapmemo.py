from functools import partial, wraps
from types import GeneratorType


def bootstrapmemo(func=None, stack=[], memo={}, args_list=[]):
    if func is None:
        return partial(bootstrapmemo, stack=stack, memo=memo, args_list=args_list)

    class _Cached:
        __slots__ = ('value',)

        def __init__(self, value):
            self.value = value

    if isinstance(memo, dict):
        def getter(t): return memo.get(t, None)
        def setter(t, x): memo[t] = x
    else:
        def getter(t): return memo[t[0]][t[1]]
        def setter(t, x): memo[t[0]][t[1]] = x

    @wraps(func)
    def wrappedfunc(*args, **kwargs):
        v = getter(args)
        if v is not None:
            return _Cached(v) if stack else v
        args_list.append(args)
        if stack:
            return func(*args, **kwargs)
        to = func(*args, **kwargs)
        while True:
            if isinstance(to, _Cached):
                to = stack[-1].send(to.value)
            elif isinstance(to, GeneratorType):
                stack.append(to)
                to = next(to)
            else:
                setter(args_list.pop(), to)
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
    return wrappedfunc
