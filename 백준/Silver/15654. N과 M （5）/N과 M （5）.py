N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res = []

def cur():
    if len(res) == M:
        print(*res)
        return

    for num in nums:
        if num not in res:
            res.append(num)
            cur()
            res.pop()


cur()