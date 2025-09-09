T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    arr = []
    for _ in range(N):
        s, e = map(int, input().split())

        for t in arr:
            ps, pe = t
            if s < ps and e > pe:
                cnt += 1
            elif s > ps and e < pe:
                cnt += 1

        arr.append((s, e))
    print(f"#{tc} {cnt}")