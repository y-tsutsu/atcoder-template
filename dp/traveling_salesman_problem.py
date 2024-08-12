from sys import maxsize


def tsp(n, cost, s=0):
    '''巡回セールスマン問題'''
    INF = maxsize
    dp = [[INF for _ in range(n)] for _ in range(1 << n)]
    dp[0][s] = 0
    for b in range(1 << n):
        for i in range(n):
            if dp[b][i] == INF:
                continue
            for ni in range(n):
                if b >> ni & 1 == 1:
                    continue
                nb = b | 1 << ni
                dp[nb][ni] = min(dp[nb][ni], dp[b][i] + cost[i][ni])
    return dp
