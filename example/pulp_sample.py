#!/usr/bin/env python3
# 線形計画法
# https://www.tellpro.net/loop0919/articles/QymeaxvTdSQiwtXSehsechwaIDHYjhKp
# https://atcoder.jp/contests/abc364/tasks/abc364_e

from sys import stdin

import pulp

_tokens = (y for x in stdin for y in x.split())
def read(): return next(_tokens)
def iread(): return int(next(_tokens))


def main():
    n, x, y = iread(), iread(), iread()
    ab = [(iread(), iread()) for _ in range(n)]
    a = [v for v, _ in ab]
    b = [v for _, v in ab]
    # モデルを作成する
    pro = pulp.LpProblem(sense=pulp.LpMaximize)
    # 変数を作成する
    p = [pulp.LpVariable(name=f'p_{i}', cat=pulp.LpBinary) for i in range(n)]  # n個について買う（1）・買わない（0）
    # 目的関数を設定する
    pro += sum(p)
    # 制約条件を設定する
    pro += sum([u * v for u, v in zip(a, p)]) <= x
    pro += sum([u * v for u, v in zip(b, p)]) <= y
    # 解を計算する
    pro.solve(pulp.PULP_CBC_CMD(msg=False))
    q = [(pulp.value(v)) for v in p]  # 算出された最適な買う（1）・買わない（0）のパターン
    ans = sum([int(v) for v in q])
    ans = min(n, ans + 1)
    print(ans)


if __name__ == '__main__':
    main()
