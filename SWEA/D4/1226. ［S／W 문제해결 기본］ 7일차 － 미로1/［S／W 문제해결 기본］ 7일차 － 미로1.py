from collections import deque

T = 10

for tc in range(1, T + 1):
    tc = int(input())
    N = 16
    maze = []
    chk = [([False] * N) for _ in range(N)]
    queue = deque()

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    for y in range(N):
        row = list(map(int, input().strip()))
        maze.append(row)

        for x, v in enumerate(row):
            if v == 2:
                queue.append([y, x])
                chk[y][x] = True

    # 0: 통로, 1: 벽, 2: 출발, 3: 도착
    def bfs(q):
        while q:
            y, x = q.popleft()

            for n in range(4):
                ny, nx = y + dy[n], x + dx[n]
                if 0 <= ny < N and 0 <= nx < N and not chk[ny][nx]:
                    nv = maze[ny][nx]
                    if nv == 3:
                        return 1
                    if nv == 0:
                        chk[ny][nx] = True
                        q.append((ny, nx))
        return 0


    print(f"#{tc}", bfs(queue))