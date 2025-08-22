T = 10

for tc in range(1, T + 1):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    res = []

    for _ in range(1, N + 1):
        tmp = input().split()
        tree[int(tmp[0])] = tmp[1:]


    def get(node: int):
        if len(tree[node]) >= 2 and tree[node][1].isdigit():
            get(int(tree[node][1]))
        res.append(tree[node][0])
        if len(tree[node]) >= 3 and tree[node][2].isdigit():
            get(int(tree[node][2]))


    get(1)
    print(f"#{tc}", ''.join(res))
