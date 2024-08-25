def recurboost(func=None, stack=[]):
    pass


class Parser:
    class Node:
        def __init__(self, d, v):
            self.d = d
            self.v = v
            self.p = []

    def __init__(self, s):
        self._s = s
        self._n = len(s)
        self._i = 0

    @recurboost
    def parse(self, d=0):
        ret = Parser.Node(d, '')
        while self._i != self._n:
            c = self._s[self._i]
            self._i += 1
            if c == '(':
                r = yield self.parse(d + 1)
                ret.p.append(r)
            elif c == ')':
                break
            else:
                ret.p.append(Parser.Node(d + 1, c))
        yield ret
