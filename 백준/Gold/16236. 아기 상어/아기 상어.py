from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

N = int(input().strip())
base = [list(map(int, input().split())) for _ in range(N)]

pos_y = pos_x = 0
s_size = 2
eat_count = 0
time_cnt = 0

for y in range(N):
    for x in range(N):
        if base[y][x] == 9:
            pos_y, pos_x = y, x
            base[y][x] = 0 
            break

def bfs_find(sy, sx, size):
    visited = [[False]*N for _ in range(N)]
    q = deque()
    q.append((sy, sx, 0))
    visited[sy][sx] = True

    min_move = -1
    tmp = []

    while q:
        y, x, d = q.popleft()

        if min_move != -1 and d > min_move:
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if visited[ny][nx]:
                continue

            target = base[ny][nx]
            if target <= size:
                visited[ny][nx] = True
                nd = d + 1
                q.append((ny, nx, nd))

                if 0 < target < size:
                    if min_move == -1:
                        min_move = nd
                    if nd == min_move:
                        tmp.append((ny, nx))

    if not tmp:
        return -1, -1, -1

    tmp.sort()
    ty, tx = tmp[0]
    return ty, tx, min_move



while True:
    ty, tx, move = bfs_find(pos_y, pos_x, s_size)
    if move == -1:
        break

    time_cnt += move
    eat_count += 1
    base[ty][tx] = 0
    pos_y, pos_x = ty, tx

    if eat_count == s_size:
        s_size += 1
        eat_count = 0

print(time_cnt)
