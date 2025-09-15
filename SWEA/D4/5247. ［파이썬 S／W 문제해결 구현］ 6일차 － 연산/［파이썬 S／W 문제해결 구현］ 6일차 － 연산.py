from collections import deque

MAXV = 10 ** 6
T = int(input())


def dfs(n, cnt) -> int:
    if n == M:
        return cnt
    if n > M + 10:
        return -1
    q.append((n, cnt))
    

    while q:
        target = q.popleft()
        t = target[0]
        d = target[1]
        for nt in (t + 1, t - 1, t * 2, t - 10):
            if 1 <= nt <= MAXV and not chk[nt]:
                if nt == M:
                    ans = d + 1
                    q.clear()
                    return ans

                chk[nt] = True
                q.append((nt, d + 1))
    return -1


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    chk = [False] * (MAXV + 1)
    chk[N] = True
    q = deque()

    print(f"#{tc} {dfs(N, 0)}")
