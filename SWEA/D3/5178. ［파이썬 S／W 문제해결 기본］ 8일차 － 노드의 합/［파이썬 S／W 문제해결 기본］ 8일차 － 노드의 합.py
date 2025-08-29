t = int(input().strip())

for tc in range(1, t + 1):
    n, m, l = map(int, input().split())
    arr = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        arr[a] = b

    for i in range(n//2, 0, -1):
        left = i * 2
        right = i * 2 + 1

        if left <= n:
            arr[i] += arr[left]
        if right <= n:
            arr[i] += arr[right]

        if i == l:
            break


    print(f"#{tc} {arr[l]}")