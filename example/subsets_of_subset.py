def main():
    p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = 0b0010101100  # 素数だけを取り出した部分集合
    print([p[i] for i in range(len(p)) if s >> i & 1 == 1])

    # 部分集合の部分集合を全列挙（1ひいてマスクしなおすのを繰り返すと全列挙できる）
    now = s
    q = []
    while True:
        q.append([p[i] for i in range(len(p)) if now >> i & 1 == 1])
        if now == 0:
            break
        now -= 1
        now &= s
    print(*q, sep='\n')


if __name__ == '__main__':
    main()
