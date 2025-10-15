N, M = map(int, input().split())
res = []


def cur():
    if len(res) == M:
        print(*res)
        return

    for i in range(1, N + 1):
        res.append(i)
        cur()
        res.pop()


cur()
