def solve(lst, n, m) -> int:
    res = 0
    for y in range(n - m + 1):
        for x in range(n - m + 1):
            s = 0
            dy = y + m
            dx = x + m
            for ny in range(y, dy):
                for nx in range(x, dx):
                    s += lst[ny][nx]
            res = max(res, s)
    return res


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(N)]

        ans = solve(arr, N, M)
        print(f"#{tc} {ans}")