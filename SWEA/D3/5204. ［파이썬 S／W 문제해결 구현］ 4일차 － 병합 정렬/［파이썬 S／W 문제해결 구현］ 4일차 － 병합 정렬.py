t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    def merge(left, right):
        result = [0] * (len(left) + len(right))
        l = r = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:          # <= 로 해도 무방
                result[l + r] = left[l]; l += 1
            else:
                result[l + r] = right[r]; r += 1
        while l < len(left):
            result[l + r] = left[l]; l += 1
        while r < len(right):
            result[l + r] = right[r]; r += 1
        return result

    def merge_sort(li):
        global ans
        if len(li) == 1:
            return li

        mid = len(li) // 2
        left_sorted  = merge_sort(li[:mid])
        right_sorted = merge_sort(li[mid:])

        if left_sorted[-1] > right_sorted[-1]:
            ans += 1

        return merge(left_sorted, right_sorted)

    sorted_arr = merge_sort(arr)
    print(f"#{tc}", sorted_arr[N // 2], ans)
