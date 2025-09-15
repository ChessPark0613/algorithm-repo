from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    adj = [[] for _ in range(N + 1)]

    for i in range(0, 2 * M, 2):
        a, b = nums[i], nums[i + 1]
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * (N + 1)
    ans = 0

    for s in range(1, N + 1):
        if visited[s]:
            continue
        ans += 1
        q = deque([s])
        visited[s] = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

    print(f"#{tc} {ans}")
