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
