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

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        V, E = map(int, input().split())
        edges = [list(map(int, input().split())) for _ in range(E)]
        edges.sort(key=lambda x: x[2])

        parents = [i for i in range(V + 1)]
        weights = [1 for _ in range(V + 1)]

        mst_cost = 0
        picked = 0

        for n1, n2, w in edges:
            if union(n1, n2):
                mst_cost += w
                picked += 1
                if picked == V:
                    break

        print(f"#{tc} {mst_cost}")