N, M = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
s = 0
left = 0

for right in range(N):
    s += arr[right]

    while s > M and left <= right:
        s -= arr[left]
        left += 1

    if s == M:
        ans += 1
        s -= arr[left]
        left += 1

print(ans)
