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
            i, j = args_list[-1]
            if memo[i][j] is not None:
                if not isinstance(to, GeneratorType):
                    stack.pop()
                i, j = args_list.pop()
                res = memo[i][j]
                to = stack[-1].send(res)
                continue
            if isinstance(to, GeneratorType):
                stack.append(to)
                to = next(to)
            else:
                i, j = args_list.pop()
                memo[i][j] = to
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
    return wrappedfunc
