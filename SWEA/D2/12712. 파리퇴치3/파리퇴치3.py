T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(N)]

    res = 0

    for y in range(N):
        for x in range(N):
            mode_1 = base[y][x]
            mode_2 = base[y][x]
            for m in range(1, M):
                if 0 <= x + m < N:
                    mode_1 += base[y][x + m]
                if 0 <= x - m < N:
                    mode_1 += base[y][x - m]
                if 0 <= y + m < N:
                    mode_1 += base[y + m][x]
                if 0 <= y - m < N:
                    mode_1 += base[y - m][x]

                if 0 <= y - m < N and 0 <= x - m < N:
                    mode_2 += base[y - m][x - m]
                if 0 <= y - m < N and 0 <= x + m < N:
                    mode_2 += base[y - m][x + m]
                if 0 <= y + m < N and 0 <= x - m < N:
                    mode_2 += base[y + m][x - m]
                if 0 <= y + m < N and 0 <= x + m < N:
                    mode_2 += base[y + m][x + m]

            if res < mode_1: res = mode_1
            if res < mode_2: res = mode_2

    print(f"#{test_case}", res)
