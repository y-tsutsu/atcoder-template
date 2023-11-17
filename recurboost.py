from functools import partial, wraps
from types import GeneratorType


def recurboost(func=None, stack=[]):
    if func is None:
        return partial(recurboost, stack=stack)

    @wraps(func)
    def wrappedfunc(*args, **kwargs):
        if stack:
            return func(*args, **kwargs)
        to = func(*args, **kwargs)
        while True:
            if isinstance(to, GeneratorType):
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
    return wrappedfunc


def recurboostmemo(func=None, stack=[], memo={}, args_list=[]):
    if func is None:
        return partial(recurboostmemo, stack=stack, memo=memo, args_list=args_list)

    @wraps(func)
    def wrappedfunc(*args, **kwargs):
        args_list.append(args)
        if stack:
            return func(*args, **kwargs)
        to = func(*args, **kwargs)
        while True:
            if args_list[-1] in memo:
                if not isinstance(to, GeneratorType):
                    stack.pop()
                res = memo[args_list.pop()]
                to = stack[-1].send(res)
                continue
            if isinstance(to, GeneratorType):
                stack.append(to)
                to = next(to)
            else:
                memo[args_list.pop()] = to
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
    return wrappedfunc


def example():
    @recurboost
    def dfs(i):
        '''再帰関数をジェネレーターで実装する．returnと再帰呼び出しの個所にyieldをつける．'''
        if i == 101:
            yield 0
        yield i + (yield dfs(i + 1))

    x = dfs(1)
    print(x)


if __name__ == '__main__':
    example()
