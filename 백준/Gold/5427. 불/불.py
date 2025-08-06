from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    w, h = map(int, input().split())
    base = [list(input().strip()) for _ in range(h)]

    queue = deque()
    fire_queue = deque()
    chk = [[False] * w for _ in range(h)]

    nx = [1, -1, 0, 0]
    ny = [0, 0, 1, -1]
    count = 0

    for y in range(h):
        for x in range(w):
            if base[y][x] == "@":
                queue.append((y, x))
                chk[y][x] = True
            elif base[y][x] == "*":
                fire_queue.append((y, x))

    escaped = False

    while queue:
        for _ in range(len(fire_queue)):
            fire_y, fire_x = fire_queue.popleft()
            for k in range(4):
                fy = fire_y + ny[k]
                fx = fire_x + nx[k]

                if 0 <= fy < h and 0 <= fx < w:
                    if base[fy][fx] == "." or base[fy][fx] == "@":
                        base[fy][fx] = "*"
                        fire_queue.append((fy, fx))

        for _ in range(len(queue)):
            y, x = queue.popleft()

            for k in range(4):
                dy = y + ny[k]
                dx = x + nx[k]

                if not (0 <= dy < h and 0 <= dx < w):
                    print(count + 1)
                    escaped = True
                    break

                if 0 <= dy < h and 0 <= dx < w:
                    if not chk[dy][dx] and base[dy][dx] == ".":
                        chk[dy][dx] = True
                        queue.append((dy, dx))
            if escaped:
                break

        if escaped:
            break
        count += 1

    if not escaped:
        print("IMPOSSIBLE")
