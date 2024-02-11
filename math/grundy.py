def grundy(n, p: list):
    '''0～nまでのGrundy数を計算．pは遷移先のリスト．ex. [5, 8]: 石を5または8個取り除く'''
    def mex(s):
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
        g[i] = mex(s)
    return g
