import sys
input = sys.stdin.readline

count = 0
maxv = 0

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

my = [-1, 0, 1, 0]
mx = [0, 1, 0, -1]

def bfs(y, x):
    res = 1
    q = [(y, x)]
    lp = 0
    while q:
        py, px = q.pop()
        for k in range(4):
            lp += 1
            cy = py + my[k]
            cx = px + mx[k]
            if 0<=cy<n and 0<=cx<m:
                if map[cy][cx] == 1 and chk[cy][cx] == False:
                    chk[cy][cx] = True
                    res += 1
                    q.append((cy, cx))
    return res



for y in range(n):
    for x in range(m):
        if map[y][x] == 1 and chk[y][x] == False:
            chk[y][x] = True
            count += 1
            maxv = max(maxv, bfs(y, x))




print(count)
print(maxv)