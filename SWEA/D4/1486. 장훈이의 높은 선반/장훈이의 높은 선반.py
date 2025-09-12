
def recur(idx, total_height):
    global min_ans

    if total_height >= B:
        min_ans = min(min_ans, total_height)
        return

    if idx == N:
        return

    recur(idx + 1, total_height + heights[idx])
    recur(idx + 1, total_height)


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_ans = 200000  # 정답 범위가 보장이면 21e8 처럼 큰값 사용 가능
    recur(0, 0)
    print(f"#{tc} {min_ans - B}")
