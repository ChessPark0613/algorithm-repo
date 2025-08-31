t = int(input())

for tc in range(1, t + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for y in range(n):
        tmp = 0
        for x in range(n):
            if puzzle[y][x] == 1:
                tmp += 1
            else:
                if tmp == k:
                    ans += 1
                tmp = 0
        if tmp == k:
            ans += 1

    for x in range(n):
        tmp = 0
        for y in range(n):
            if puzzle[y][x] == 1:
                tmp += 1
            else:
                if tmp == k:
                    ans += 1
                tmp = 0
        if tmp == k:
            ans += 1

    print(f"#{tc}", ans)
