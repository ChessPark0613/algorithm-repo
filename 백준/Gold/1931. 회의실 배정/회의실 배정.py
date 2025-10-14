N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))
ans = 0
prev_end_time = 0

for meet in meetings:
    start = meet[0]
    end = meet[1]

    if prev_end_time <= start:
        prev_end_time = end
        ans += 1

print(ans)