T = int(input())

for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    ans = 0

    def chk(cnt):
        if any(c >= 3 for c in cnt):
            return True
        for i in range(8):
            if cnt[i] and cnt[i + 1] and cnt[i + 2]:
                return True
        return False

    for i, num in enumerate(nums):
        if i % 2 == 0:
            p1[num] += 1
        else:
            p2[num] += 1
        c1 = chk(p1)
        c2 = chk(p2)

        if c1 and c2:
            ans = 0
            break
        elif c1:
            ans = 1
            break
        elif c2:
            ans = 2
            break

    print(f"#{tc} {ans}")

