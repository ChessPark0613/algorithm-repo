N, K = map(int, input().split())

MAX = 100001
visited = [0] * MAX

queue = [N]
front = 0
res = 0

while front < len(queue):
    now = queue[front]
    front += 1

    if now == K:
        res = visited[now]
        break

    for next_pos in (now - 1, now + 1, now * 2):
        if 0 <= next_pos < MAX and visited[next_pos] == False:
            visited[next_pos] = visited[now] + 1
            queue.append(next_pos)

print(res)
