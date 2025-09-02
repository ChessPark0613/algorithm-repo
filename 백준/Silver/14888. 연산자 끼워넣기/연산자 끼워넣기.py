import sys
input = sys.stdin.readline

def dfs(idx, cur, a, s, m, d):
    global maxv, minv
    if idx == n:
        maxv = max(maxv, cur)
        minv = min(minv, cur)
        return

    if a > 0:
        dfs(idx + 1, cur + arr[idx], a - 1, s, m, d)
    if s > 0:
        dfs(idx + 1, cur - arr[idx], a, s - 1, m, d)
    if m > 0:
        dfs(idx + 1, cur * arr[idx], a, s, m - 1, d)
    if d > 0:
        if cur < 0:
            dfs(idx + 1, -(int(-cur // arr[idx])), a, s, m, d - 1)
        else:
            dfs(idx + 1, int(cur // arr[idx]), a, s, m, d - 1)




if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())

    maxv = -10**9
    minv = 10**9

    dfs(1, arr[0], add, sub, mul, div)
    
    print(maxv)
    print(minv)