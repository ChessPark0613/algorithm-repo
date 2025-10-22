N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N
line = [-1] * N
res = []

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            line[i] = j

prev_idx = dp.index(max(dp))

while prev_idx > -1:
    res.append(nums[prev_idx])
    prev_idx = line[prev_idx]

print(max(dp))
print(*reversed(res))
