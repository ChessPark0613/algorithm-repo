T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    cargo = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    cargo.sort(reverse=True)
    truck.sort(reverse=True)
    i = j = 0
    ans = 0

    while i < n and j < m:
        if cargo[i] <= truck[j]:
            ans += cargo[i]
            i += 1
            j += 1
        else:
            i += 1

    print(f"#{tc}", ans)
