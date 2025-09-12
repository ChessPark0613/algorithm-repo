T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    n = N * N
    chk = [1] * n
    min_v = 0
    cnt = 0

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    for y in range(N):
        for x in range(N):
            target = arr[y][x]
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]

                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                if target + 1 == arr[ny][nx]:
                    chk[target] += 1

    for i in range(1, n - 1):
        if chk[i] == 2:
            tmp = 2
            j = i + 1
            while j < n and chk[j] == 2:
                tmp += 1
                chk[j] = 0
                j += 1

            if tmp > cnt:
                cnt = tmp
                min_v = i

    print(f"#{tc} {min_v} {cnt}")

