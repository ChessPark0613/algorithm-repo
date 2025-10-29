def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if weights[ra] < weights[rb]:
        ra, rb = rb, ra
    parents[rb] = ra
    weights[ra] += weights[rb]
    return True

N, M = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(N)]
already = [list(map(int, input().split())) for _ in range(M)]

parents = list(range(N))
weights = [1] * N

for x, y in already:
    union(x - 1, y - 1)

edges = []
for i in range(N):
    x1, y1 = cost[i]
    for j in range(i + 1, N):
        x2, y2 = cost[j]
        dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        edges.append((i, j, dist))

edges.sort(key=lambda x: x[2])

mst_cost, picked = 0, 0
for n1, n2, w in edges:
    if union(n1, n2):
        mst_cost += w
        picked += 1
        if picked == N - 1:
            break

print(f"{mst_cost:.2f}")
