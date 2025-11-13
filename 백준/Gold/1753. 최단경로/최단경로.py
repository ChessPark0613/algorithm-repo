import sys
input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
max_w = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    max_w = max(max_w, w)

dist = [INF] * (V + 1)
dist[start] = 0

bucket = [ [] for _ in range(max_w * V + 1) ]

bucket[0].append(start)
idx = 0

while idx <= max_w * V:
    while idx <= max_w * V and not bucket[idx]:
        idx += 1
    if idx > max_w * V:
        break

    u = bucket[idx].pop()
    if idx > dist[u]:
        continue

    for v, w in graph[u]:
        nd = dist[u] + w
        if nd < dist[v]:
            old = dist[v]
            dist[v] = nd
            bucket[nd].append(v)

for i in range(1, V + 1):
    print(dist[i] if dist[i] < INF else "INF")
