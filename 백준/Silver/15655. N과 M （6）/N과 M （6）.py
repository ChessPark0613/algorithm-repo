N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res = []


def cur(idx):
    if len(res) == M:
        print(*res)
        return

    for i in range(idx, N):
        if nums[i] not in res:
            res.append(nums[i])
            cur(i)
            res.pop()


cur(0)
