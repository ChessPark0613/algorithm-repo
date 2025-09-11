T = int(input().strip())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    M = [0] + arr[1:]

    pos = 1
    ans = 0

    while pos + M[pos] < N:
        nxt = pos + M[pos]
        test = pos + 1
        best = test + M[test] # 여기서 도착하면 끝

        for n in range(pos + 2, N + 1):
            if n > nxt:
                break

            if n + M[n] > best:
                test = n
                best = n + M[n]

        pos = test
        ans += 1
    print(f"#{tc} {ans}")