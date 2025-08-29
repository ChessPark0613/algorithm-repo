t = int(input())
for tc in range(1, t + 1):
    n = int(input().strip())
    arr = list(map(int, input().split()))

    hip = [0]

    for x in arr:
        hip.append(x)
        i = len(hip) - 1
        while i > 1 and hip[i] < hip[i // 2]:
            hip[i], hip[i // 2] = hip[i // 2], hip[i]
            i //= 2

    i = len(hip) - 1
    res = 0
    i //= 2
    while i > 0:
        res += hip[i]
        i //= 2

    print(f"#{tc} {res}")
