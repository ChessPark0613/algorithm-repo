T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    ans = 0
    if arr[-1] < 3:
        ans = -1
    else:
        for i in (2, 1):
            if arr[i] <= arr[i - 1]:
                t = arr[i] - 1
                if t < 1:
                    ans = -1
                    break
                ans += (arr[i - 1] - t)
                arr[i - 1] = t

    print(f"#{tc}", ans)