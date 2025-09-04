def solve(n, lst):
    dp = [0] * n
    dp[0] = lst[0][0]
    for i in range(1, n):
        dp[i] = dp[i - 1] + lst[0][i]

    for y in range(1, n):
        dp[0] += lst[y][0]
        for x in range(1, n):
            dp[x] = lst[y][x] + min(dp[x], dp[x - 1])

    return dp[n - 1]


if __name__ == "__main__":
    T = int(input().strip())

    for tc in range(1, T + 1):
        N = int(input().strip())
        base = [list(map(int, input().split())) for _ in range(N)]
        ans = solve(N, base)

        print(f"#{tc} {ans}")
