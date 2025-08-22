mo = set("aeiou")
L, C = map(int, input().split())
base = input().split()
base.sort()

snap = []
res = []


def dfs(start, depth, vcnt, ccnt):
    if depth == L:
        if vcnt >= 1 and ccnt >= 2:
            res.append(''.join(snap))
            return

    for i in range(start, C):
        ch = base[i]
        snap.append(ch)
        if ch in mo:
            dfs(i + 1, depth + 1, vcnt + 1, ccnt)
        else:
            dfs(i + 1, depth + 1, vcnt, ccnt + 1)
        snap.pop()

dfs(0, 0, 0, 0)
[print(x) for x in res]
