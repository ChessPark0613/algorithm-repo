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


N = int(input())
cost_map = [list(map(int, input().split())) for _ in range(N)]
edges = []

parents = list(range(N + 1))
weights = [1] * (N + 1)

mst_cost = 0
picked = 0

for y in range(N):
    for x in range(y + 1, N):
        edges.append([y, x, cost_map[y][x]])

edges.sort(key=lambda x: x[2])

for n1, n2, w in edges:
    if union(n1, n2):
        mst_cost += w
        picked += 1
        if picked == N - 1:
            break

print(mst_cost)
