N, S = map(int, input().split())
base = list(map(int, input().split()))

ans = 0

def dfs(idx: int, total: int, p: int):
    global ans
    if idx == N:
        if total == S and p > 0:
            ans += 1
        return
    dfs(idx + 1, total + base[idx], p + 1)
    dfs(idx + 1, total, p)

dfs(0, 0, 0)
print(ans)