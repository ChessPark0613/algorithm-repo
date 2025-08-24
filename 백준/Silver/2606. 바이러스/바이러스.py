N = int(input())
node_count = int(input())
nodes = [[] for _ in range(N + 1)]
chk = [False] * (N + 1)
ans = 0
stack = []

for _ in range(node_count):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

def dfs(index: int):
    global ans
    for n in nodes[index]:
        if not chk[n]:
            ans += 1
            chk[n] = True
            dfs(n)

chk[1] = True
dfs(1)
print(ans)
