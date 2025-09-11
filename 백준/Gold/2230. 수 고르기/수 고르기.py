N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()

ans = float("inf")
left = right = 0

while left < N and right < N:
    diff = nums[right] - nums[left]
    if diff >= M:
        ans = min(ans, diff)
        left += 1
    else:
        right += 1
    if left > right:
        right = left

print(ans)
