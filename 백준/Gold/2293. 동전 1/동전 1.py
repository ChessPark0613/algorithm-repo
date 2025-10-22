N, K = map(int, input().split())
cost = [int(input()) for _ in range(N)]

dp = [0] * (K + 1)
dp[0] = 1

for coin in cost:
    for i in range(coin, K + 1):
        dp[i] = dp[i] + dp[i - coin]

print(dp[K])