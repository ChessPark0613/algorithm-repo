T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    sell = 0

    while arr:
        t = arr.index(max(arr))
        if t == 0:
            arr = arr[1:]
        else:
            sell += (arr[t] * t) - sum(arr[:t])
            arr = arr[t + 1:]
    print(f"#{tc} {sell}")