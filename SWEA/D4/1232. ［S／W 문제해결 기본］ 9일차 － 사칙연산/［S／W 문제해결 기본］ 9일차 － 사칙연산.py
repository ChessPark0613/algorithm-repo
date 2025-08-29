T = 10

for tc in range(1, T + 1):
    n = int(input())
    arr = [0] * (n + 1)
    e = []
    for _ in range(n):
        tmp = list(map(str, input().split()))
        if len(tmp) > 2:
            e.append((int(tmp[0]), tmp[1], int(tmp[2]), int(tmp[3])))
        else:
            arr[int(tmp[0])] = int(tmp[1])

    while e:
        i, s, l, r = e.pop()
        vl = arr[l]
        vr = arr[r]
        if s == '+':
            arr[i] = vl + vr
        elif s == '-':
            arr[i] = vl - vr
        elif s == '*':
            arr[i] = vl * vr
        elif s == '/':
            arr[i] = vl / vr


    print(f"#{tc}", int(arr[1]))
