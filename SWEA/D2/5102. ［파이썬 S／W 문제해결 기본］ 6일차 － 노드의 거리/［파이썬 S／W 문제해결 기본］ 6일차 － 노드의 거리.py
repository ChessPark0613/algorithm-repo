from collections import deque

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    nodes = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    S, G = map(int, input().split())

    def bfs():
        queue = deque([S])
        chk = [False] * (V + 1)
        chk[S] = True
        c = 0

        while queue:
            for _ in range(len(queue)):
                now = queue.popleft()
                if now == G:
                    return c
                for nxt in nodes[now]:
                    if not chk[nxt]:
                        chk[nxt] = True
                        queue.append(nxt)
            c += 1

        return 0

    print(f"#{tc}", bfs())
