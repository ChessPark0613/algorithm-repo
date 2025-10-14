import heapq as hq

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x: x[0])

running = []

for start, end in times:
    if running and running[0] <= start:
        hq.heapreplace(running, end)
    else:
        hq.heappush(running, end)  # 새 강의실 하나 추가

print(len(running))
