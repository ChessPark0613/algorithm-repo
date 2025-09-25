def can_set(house, c, dist):
    count = 1
    last = house[0]

    for i in range(1, len(house)):
        if house[i] - last >= dist:
            count += 1
            last = house[i]
    return count >= c


n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

left, right = 1, house[-1] - house[0]
result = 0

while left <= right:
    mid = (left + right) // 2
    if can_set(house, c, mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
