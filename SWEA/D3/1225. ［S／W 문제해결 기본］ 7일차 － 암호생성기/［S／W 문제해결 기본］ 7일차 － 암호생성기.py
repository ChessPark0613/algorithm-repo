from collections import deque

T = 10

for tc in range(1, T + 1):
    t = int(input())
    queue = deque(map(int, input().split()))

    while True:
        for i in range(1, 6):
            num = queue.popleft() - i
            if num <= 0:
                queue.append(0)
                break
            else:
                queue.append(num)
        if queue[-1] == 0:
            break

    print(f"#{tc}", *queue)
