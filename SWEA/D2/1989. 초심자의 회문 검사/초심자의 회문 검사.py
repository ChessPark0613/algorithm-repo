T = int(input())

for test_case in range(1, T + 1):
    base = list(map(str, input()))
    N = len(base)
    res = 1

    for x in range(N // 2):
        if base[x] != base[N - 1 - x]:
            res = 0
            break

    print(f"#{test_case}", res)
