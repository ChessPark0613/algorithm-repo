from collections import deque

T = 10

for tc in range(1, T + 1):
    l = int(input())
    base = list(map(str, input()))

    stack = deque()
    n = deque()

    for b in base:
        try:
            nb = int(b)
            n.append(nb)
            if stack:
                n.append(stack.popleft())
        except:
            stack.append(b)

    for i in range(l//2):
        a = int(n.popleft())
        b = int(n.popleft())
        sign = n.popleft()
        n.appendleft(b + a)

    print(f"#{tc}",n[0])
