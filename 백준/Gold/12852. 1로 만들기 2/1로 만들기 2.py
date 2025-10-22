N = int(input())

dp = [1] * (N + 1)
prev = [-1] * (N + 1)
res = [N]

for i in range(1, N + 1):
    if i * 2 < N + 1 and (dp[i * 2] == 1 or dp[i * 2] > dp[i] + 1):
        dp[i * 2] = dp[i] + 1
        prev[i * 2] = i

    if i * 3 < N + 1 and (dp[i * 3] == 1 or dp[i * 3] > dp[i] + 1):
        dp[i * 3] = dp[i] + 1
        prev[i * 3] = i

    if i + 1 < N + 1 and (dp[i + 1] == 1 or dp[i + 1] > dp[i] + 1):
        dp[i + 1] = dp[i] + 1
        prev[i + 1] = i


length = dp[N] - 1
prev_idx = prev[N]

while prev_idx > -1:
    res.append(prev_idx)
    prev_idx = prev[prev_idx]

print(length)
print(*res)
