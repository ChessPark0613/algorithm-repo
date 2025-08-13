dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]

    res = -1


    def dfs(sy, sx, vector, lst):
        global res
        if vector == 2 and res >= 2 * len(lst): return

        lst_1 = lst + [base[sy][sx]]
        for v in [vector, (vector + 1)]:
            if v < 4:
                ny = sy + dy[v]
                nx = sx + dx[v]
                if ny == y and nx == x and v == 3:
                    res = max(res, len(lst_1))
                    return
                if 0 <= ny < N and 0 <= nx < N:
                    if base[ny][nx] not in lst_1:
                        dfs(ny, nx, v, lst_1)


    for y in range(N):
        for x in range(N):
            if y < N - 2 and 0 < x < N - 1:
                dfs(y, x, 0, [])

    print(f"#{test_case}", res)
