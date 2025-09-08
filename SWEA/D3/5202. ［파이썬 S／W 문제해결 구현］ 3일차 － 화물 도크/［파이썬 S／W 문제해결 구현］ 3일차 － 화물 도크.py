T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    cargo = [tuple(map(int, input().split())) for _ in range(N)]
    cargo.sort(key=lambda x: (x[1], x[0]))
    last_end = -1
    ans = 0
    
    for s, e in cargo:
        if s >= last_end:
            ans += 1
            last_end = e

    print(f"#{tc} {ans}")
