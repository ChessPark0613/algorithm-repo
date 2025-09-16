def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]

def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))

    edges.sort()
    parent = [i for i in range(V + 1)]

    mst_cost = 0
    for w, n1, n2 in edges:
        if find_parent(parent, n1) != find_parent(parent, n2):
            union_parent(parent, n1, n2)
            mst_cost += w

    print(f"#{tc} {mst_cost}")
