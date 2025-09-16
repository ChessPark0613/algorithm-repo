from heapq import heappush, heappop

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
INF = float("inf")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]

    while pq:
        t, y, x = heappop(pq)

        if (y, x) == (N - 1, N - 1):
            break

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                add = 0
                if H[ny][nx] > H[y][x]:
                    add = H[ny][nx] - H[y][x]

                nt = t + 1 + add

                if nt < dist[ny][nx]:
                    dist[ny][nx] = nt
                    heappush(pq, (nt, ny, nx))

    print(f"#{tc}", dist[N - 1][N - 1])
