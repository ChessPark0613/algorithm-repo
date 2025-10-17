n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

res = []

def cur(idx):
    if len(res) == m:
        print(*res)
        return

    for i in range(idx, n):
        res.append(nums[i])
        cur(i)
        res.pop()


cur(0)