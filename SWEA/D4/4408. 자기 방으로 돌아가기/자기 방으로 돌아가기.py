T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [0] * 201

    for _ in range(N):
        s, e = map(int, input().split())
        u = (s + 1) // 2
        v = (e + 1) // 2
        L, R = sorted((u, v))
        for i in range(L, R + 1):
            rooms[i] += 1

    print(f"#{tc} {max(rooms)}")
