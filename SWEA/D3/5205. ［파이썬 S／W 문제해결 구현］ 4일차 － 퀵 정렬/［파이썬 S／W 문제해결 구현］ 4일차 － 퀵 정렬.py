T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))


    def partition(start, end):
        p = arr[start]
        i = start
        j = end
        while i <= j:
            while i <= j and arr[i] <= p:
                i += 1
            while i <= j and arr[j] > p:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[start], arr[j] = arr[j], arr[start]

        return j


    def qs(start, end):
        if start >= end:
            return
        p = partition(start, end)
        qs(start, p - 1)
        qs(p + 1, end)


    qs(0, N - 1)
    print(f"#{tc} {arr[N // 2]}")
