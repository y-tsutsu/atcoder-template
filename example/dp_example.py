from itertools import accumulate


def lcs(s, t):
    '''最長共通部分列'''
    dp = [0 for _ in range(len(t) + 1)]
    for i in range(1, len(s) + 1):
        p = [0 for _ in range(len(t) + 1)]
        dp, p = p, dp
        for j in range(1, len(t) + 1):
            dp[j] = max(p[j], dp[j - 1])
            if s[i - 1] == t[j - 1]:
                dp[j] = max(dp[j], p[j - 1] + 1)
    return dp[-1]


def ed(s, t):
    '''編集距離 s -> t'''
    INSERT_COST, DELETE_COST, CHANGE_COST = 1, 1, 1
    dp = [i for i in range(len(t) + 1)]
    for i in range(1, len(s) + 1):
        p = [i for _ in range(len(t) + 1)]
        dp, p = p, dp
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[j] = min(p[j] + DELETE_COST, dp[j - 1] + INSERT_COST, p[j - 1])
            else:
                dp[j] = min(p[j] + DELETE_COST, dp[j - 1] + INSERT_COST, p[j - 1] + CHANGE_COST)
    return dp[-1]


def lis(a):
    '''最長増加部分列'''
    from bisect import bisect_left
    n = len(a)
    dp = [0 for _ in range(n)]
    d = []
    for i in range(n):
        j = bisect_left(d, a[i])
        dp[i] = j + 1
        if j == len(d):
            d.append(a[i])
        else:
            d[j] = min(d[j], a[i])
    return max(dp)


def count_sum_num(value, count, min_, max_):
    '''整数をcount個まで選んで総和がvalue以下になる場合の数（使える数字はmin_～max_）
    dp[i][j]: 整数をi個選んでjをつくる場合の数'''
    dp = [[0 for _ in range(value + 1)] for _ in range(count + 1)]
    dp[0][0] = 1
    for i in range(count):
        acm = list(accumulate(dp[i], initial=0))
        for j in range(value + 1):
            s = max(0, j - max_)
            e = max(-1, j - min_)
            dp[i + 1][j] = acm[e + 1] - acm[s]
    return dp
