n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

res = []

def cur():
    if len(res) == m:
        print(*res)
        return

    for num in nums:
        res.append(num)
        cur()
        res.pop()


cur()