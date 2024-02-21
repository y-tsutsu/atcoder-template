from functools import partial, wraps
from types import GeneratorType


def recurboostmemolist(func=None, stack=[], memo=[[None]], args_list=[]):
    if func is None:
        return partial(recurboostmemolist, stack=stack, memo=memo, args_list=args_list)

    @wraps(func)
    def wrappedfunc(*args, **kwargs):
        args_list.append(args)
        if stack:
            return func(*args, **kwargs)
        to = func(*args, **kwargs)
        while True:
            t = args_list[-1]
            v = memo[t[0]][t[1]]
            if v is not None:
                if not isinstance(to, GeneratorType):
                    stack.pop()
                args_list.pop()
                to = stack[-1].send(v)
                continue
            if isinstance(to, GeneratorType):
                stack.append(to)
                to = next(to)
            else:
                args_list.pop()
                memo[t[0]][t[1]] = to
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
    return wrappedfunc
