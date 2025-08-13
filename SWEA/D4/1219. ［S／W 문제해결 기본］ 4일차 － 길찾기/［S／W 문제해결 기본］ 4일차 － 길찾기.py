T = 10

for _ in range(1, T + 1):
    tc, length = map(int, input().split())
    tmp = list(map(int, input().split()))
    base = [[] for _ in range(100)]
    is_go = False

    for i in range(length * 2):
        if i % 2 == 0:
            base[tmp[i]].append(tmp[i + 1])

    stack = [base[0]]
    while stack:
        p = stack.pop()
        for s in p:
            stack.append(base[s])
            if s == 99:
                is_go = True
                stack.clear()
                break

    print(f"#{tc}", int(is_go))

