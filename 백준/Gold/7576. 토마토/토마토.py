from collections import deque

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

queue = [(i, j) for i in range(N) for j in range(M) if tomatoes[i][j] == 1]
count = len(queue)

nx = [1, -1, 0, 0]
ny = [0, 0, -1, 1]

count_day = 0

while queue:
    queue2 = deque(queue)
    queue.clear()

    while queue2:
        y, x = queue2.popleft()

        for d in range(4):
            dy = y + ny[d]
            dx = x + nx[d]

            if 0 <= dy < N and 0 <= dx < M:
                if tomatoes[dy][dx] == 0:
                    tomatoes[dy][dx] = 1
                    queue.append((dy, dx))
    if queue:
        count_day += 1

if any(0 in row for row in tomatoes):
    count_day = -1

print(count_day)
