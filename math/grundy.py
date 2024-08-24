from typing import Callable


def grundyf(n, f: Callable):
    '''0～nまでのGrundy数を計算. fは遷移先のリストを返す関数'''
    def _mex(s):
        for i in range(len(s)):
            if i not in s:
                return i
        return len(s)

    g = [0 for _ in range(n + 1)]
    for i in range(len(g)):
        s = set()
        for j in f(i):
            s.add(g[j])
        g[i] = _mex(s)
    return g


def grundyp(n, p: list):
    '''0～nまでのGrundy数を計算. pは遷移先へのコストのリスト. ex. [5, 8]: 石を5または8個取り除く'''
    def _mex(s):
        for i in range(len(s)):
            if i not in s:
                return i
        return len(s)

    g = [0 for _ in range(n + 1)]
    for i in range(len(g)):
        s = set()
        for v in p:
            j = i - v
            if j < 0:
                continue
            s.add(g[j])
        g[i] = _mex(s)
    return g


def grundylr(n, le, ri):
    '''0～nまでのGrundy数を計算. 遷移は[le, ri]の範囲で石を取り除く. この場合は周期性があり計算可能'''
    def _grundy(x): (x % (le + ri)) // le
    g = [_grundy(i) for i in range(n + 1)]
    return g
