T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    ans = 0
    for mask in range(1, 1 << N):
        s = 0
        for i in range(N):
            if (mask >> i) & 1:
                s += nums[i]
        if s == K:
            ans += 1

    print(f"#{tc} {ans}")
