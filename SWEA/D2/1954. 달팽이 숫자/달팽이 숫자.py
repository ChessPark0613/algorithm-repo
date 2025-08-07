T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    x = 0
    y = 0
    k = 0
    
    for i in range(1, N * N + 1):
        arr[y][x] = i
        nx = x + dx[k]
        ny = y + dy[k]

        if not (0 <= nx < N and 0 <= ny < N and arr[ny][nx] == 0):
            k = (k + 1) % 4
            nx = x + dx[k]
            ny = y + dy[k]

        x, y = nx, ny

    print(f"#{test_case}")
    for a in arr:
        print(*a)