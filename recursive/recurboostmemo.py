from functools import partial, wraps
from types import GeneratorType


def recurboostmemo(func=None, stack=[], memo={}, args_list=[]):
    if func is None:
        return partial(recurboostmemo, stack=stack, memo=memo, args_list=args_list)

    if isinstance(memo, dict):
        def getter(t): return memo.get(t, None)
        def setter(t, x): memo[t] = x
    else:
        def getter(t): return memo[t[0]][t[1]]
        def setter(t, x): memo[t[0]][t[1]] = x

    @wraps(func)
    def wrappedfunc(*args, **kwargs):
        args_list.append(args)
        if stack:
            return func(*args, **kwargs)
        to = func(*args, **kwargs)
        while True:
            v = getter(args_list[-1])
            if v is not None:
                if not isinstance(to, GeneratorType):
                    stack.pop()
                args_list.pop()
                if not stack and not args_list:
                    return v
                to = stack[-1].send(v)
                continue
            if isinstance(to, GeneratorType):
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
