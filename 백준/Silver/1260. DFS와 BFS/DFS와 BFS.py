from collections import deque

N, M, V = map(int, input().split())
base = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    base[a].append(b)
    base[b].append(a)


def dfs():
    chk = [False] * (N + 1)
    stack = [V]
    res = []
    while stack:
        u = stack.pop()
        if chk[u]:
            continue
        chk[u] = True
        res.append(u)
        for v in sorted(base[u], reverse=True):
            if not chk[v]:
                stack.append(v)
    return res


def bfs():
    chk = [False] * (N + 1)
    queue = deque([V])
    res = []
    while queue:
        u = queue.popleft()
        if chk[u]:
            continue
        chk[u] = True
        res.append(u)
        for v in sorted(base[u]):
            if not chk[v]:
                queue.append(v)
    return res


print(*dfs())
print(*bfs())
