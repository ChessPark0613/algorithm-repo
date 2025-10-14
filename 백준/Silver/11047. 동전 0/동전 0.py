N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
ans = 0

for coin in reversed(coins):
    if coin <= K:
        cnt = K // coin
        ans += cnt
        K -= coin * cnt

    if K == 0:
        break

print(ans)