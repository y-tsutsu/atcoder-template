from functools import partial, wraps
from types import GeneratorType


def recurboostmemo(func=None, stack=[], memo={}, args_list=[]):
    if func is None:
        return partial(recurboostmemo, stack=stack, memo=memo, args_list=args_list)

    @wraps(func)
    def wrappedfunc(*args, **kwargs):
        def _key(a): return a[0] if len(a) == 1 else a
        args_list.append(args)
        if stack:
            return func(*args, **kwargs)
        memo.clear()
        to = func(*args, **kwargs)
        while True:
            k = _key(args_list[-1])
            m = memo.get(k, None)
            if m is not None:
                if not isinstance(to, GeneratorType):
                    stack.pop()
                args_list.pop()
                res = m
                to = stack[-1].send(res)
                continue
            if isinstance(to, GeneratorType):
                stack.append(to)
                to = next(to)
            else:
                args_list.pop()
                memo[k] = to
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
    return wrappedfunc
