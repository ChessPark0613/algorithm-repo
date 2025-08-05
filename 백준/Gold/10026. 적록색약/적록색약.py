N = int(input())
pic = [list(input()) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x, chk, is_weak):
    queue = [(y, x)]
    chk[y][x] = True
    color = pic[y][x]

    while queue:
        cy, cx = queue.pop(0)
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not chk[ny][nx]:
                next_color = pic[ny][nx]

                if not is_weak and next_color == color:
                    chk[ny][nx] = True
                    queue.append((ny, nx))

                elif is_weak:
                    if color in ("R", "G") and next_color in ("R", "G"):
                        chk[ny][nx] = True
                        queue.append((ny, nx))
                    elif color == "B" and next_color == "B":
                        chk[ny][nx] = True
                        queue.append((ny, nx))

chk_normal = [[False]*N for _ in range(N)]
res_normal = 0
for i in range(N):
    for j in range(N):
        if not chk_normal[i][j]:
            bfs(i, j, chk_normal, is_weak=False)
            res_normal += 1

chk_weak = [[False]*N for _ in range(N)]
res_weak = 0
for i in range(N):
    for j in range(N):
        if not chk_weak[i][j]:
            bfs(i, j, chk_weak, is_weak=True)
            res_weak += 1

print(res_normal, res_weak)
