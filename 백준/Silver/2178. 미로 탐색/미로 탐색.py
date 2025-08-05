
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
chk = [[False] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

queue = [(0, 0)]
chk[0][0] = True

while queue:
    y, x = queue[0]
    queue = queue[1:]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if maze[ny][nx] == 1 and not chk[ny][nx]:
                maze[ny][nx] = maze[y][x] + 1
                chk[ny][nx] = True
                queue.append((ny, nx))

print(maze[N-1][M-1])
