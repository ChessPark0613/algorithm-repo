import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input().strip())
    graph = [0] + list(map(int, input().split()))
    child = [0] * (N + 1)

    for i in range(1, N + 1):
        child[graph[i]] += 1

    leaves = deque(i for i in range(1, N + 1) if child[i] == 0)
    cnt = 0

    while leaves:
        leaf = leaves.popleft()
        cnt += 1
        nxt = graph[leaf]
        child[nxt] -= 1
        if child[nxt] == 0:
            leaves.append(nxt)

    print(cnt)
