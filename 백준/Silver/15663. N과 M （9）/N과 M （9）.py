N, M = map(int, input().split())
base = sorted(map(int, input().split()))

used = [False] * N
tmp = []
res = []

def dfs(depth):
    if depth == M:
        res.append(tmp.copy())
        return

    prev = None
    for i in range(N):
        if used[i]:
            continue
        if prev == base[i]:
            continue

        used[i] = True
        tmp.append(base[i])
        dfs(depth + 1)
        tmp.pop()
        used[i] = False
        prev = base[i]

dfs(0)

for seq in res:
    print(*seq)
