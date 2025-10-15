N, M = map(int, input().split())
res = []


def cur(x):
    if len(res) == M:
        print(*res)
        return

    for i in range(x, N + 1):
        if i not in res:
            res.append(i)
            cur(i + 1)
            res.pop()


cur(1)