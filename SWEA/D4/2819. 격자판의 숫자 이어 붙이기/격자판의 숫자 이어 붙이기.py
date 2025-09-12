from collections import deque

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    q = deque([(1, x, y, arr[x][y])])
    while q:
        l, i, j, num = q.popleft()
        if l == 7:
            answer.add(num)
        else:
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < 4 and 0 <= nj < 4: q.append((l + 1, ni, nj, num + arr[ni][nj]))


T = int(input())
for tc in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    answer = set()
    for x in range(4):
        for y in range(4):
            bfs(x, y)
    print(f'#{tc} {len(answer)}')
