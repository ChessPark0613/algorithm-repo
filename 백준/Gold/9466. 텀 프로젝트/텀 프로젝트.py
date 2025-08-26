T = int(input())
for _ in range(T):
    n = int(input().strip())
    nodes = [0] + list(map(int, input().split()))

    chk = [0] * (n + 1)
    res = n

    for i in range(1, n + 1):
        if chk[i]:
            continue

        stack = []
        pos = {}
        v = i

        while True:
            if chk[v]:
                while stack:
                    u = stack.pop()
                    chk[u] = 1
                    pos.pop(u, None)
                break

            if v in pos:
                start = pos[v]
                res -= (len(stack) - start)

                while stack:
                    u = stack.pop()
                    chk[u] = 1
                    pos.pop(u, None)
                break

            pos[v] = len(stack)
            stack.append(v)

            nv = nodes[v]
            if chk[nv]:
                while stack:
                    u = stack.pop()
                    chk[u] = 1
                    pos.pop(u, None)
                break

            v = nv

    print(res)
