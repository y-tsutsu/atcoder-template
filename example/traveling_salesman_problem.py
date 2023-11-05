from sys import maxsize


def tsp(n, cost):
    '''巡回セールスマン問題'''
    INF = maxsize
    dp = [[INF for _ in range(n)] for _ in range(1 << n)]
    dp[0][0] = 0
    for s in range(1 << n):
        for i in range(n):
            if dp[s][i] == INF:
                continue
            for ni in range(n):
                if s >> ni & 1 == 1:
                    continue
                ns = s | 1 << ni
                dp[ns][ni] = min(dp[ns][ni], dp[s][i] + cost[i][ni])
