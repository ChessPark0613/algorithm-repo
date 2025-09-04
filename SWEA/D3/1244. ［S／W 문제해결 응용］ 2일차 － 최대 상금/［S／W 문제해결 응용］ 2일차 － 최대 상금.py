if __name__ == "__main__":
    T = int(input().strip())
    for tc in range(1, T + 1):
        nums, n = input().split()
        n = int(n)
        nums = list(nums)
        target = sorted(nums, reverse=True)
        l = len(target)

        while n > 0:
            for i in range(l):
                if target[i] != nums[i]:
                    if nums[target.index(nums[i])] == target[i]:
                        index = target.index(nums[i])
                    else:
                        index = "".join(nums).rindex(target[i])
                    nums[i], nums[index] = nums[index], nums[i]
                    n -= 1
                    break

            else:
                if n % 2 == 0:
                    break
                else:
                    dummy = l - 1
                    for d in range(1, l):
                        if nums[d - 1] == nums[d]:
                            dummy = d
                            nums[dummy - 1], nums[dummy] = nums[dummy], nums[dummy - 1]
                            break
                    nums[dummy - 1], nums[dummy] = nums[dummy], nums[dummy - 1]
                    n -= 1
        ans = ''
        for n in nums:
            ans += n
        print(f"#{tc} {ans}")
