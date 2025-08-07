T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    base = list(map(int, input().split()))

    def s(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    sorted_base = s(base)

    print(f"#{test_case}", *sorted_base)
