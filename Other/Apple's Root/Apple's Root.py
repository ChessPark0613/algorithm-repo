T = int(input())
def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solve(apples):
    N = len(apples)
    used = [False] * N
    order = [0] * N   # 현재까지 만든 순서

    def dfs(depth, cur_pos, cost):
        global best
        if depth == N:
            best = min(best, cost + manhattan(cur_pos, (0,0)))
            return
        for i in range(N):
            if not used[i]:
                used[i] = True
                order[depth] = i           # (0,1,2) 처럼 순서가 쌓임
                next_cost = cost + manhattan(cur_pos, apples[i])
                dfs(depth + 1, apples[i], next_cost)
                used[i] = False            # 백트레킹(원상복구)


    dfs(0, (0,0), 0)
    return best

for tc in range(1, T + 1):
    N = int(input())
    apples = [tuple(map(int, input().split())) for _ in range(N)]
    best = float('inf')
    ans = min(best ,solve(apples))
    print(f"#{tc} {ans}")
