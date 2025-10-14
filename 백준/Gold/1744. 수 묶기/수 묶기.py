import heapq as hq

m_arr = []
p_arr = []
zero_cnt = 0
ans = 0

N = int(input())
for _ in range(N):
    i = int(input())
    if i < 0:
        hq.heappush(m_arr, i)
    elif i == 0:
        zero_cnt += 1
    else:
        p_arr.append(i)

p_arr.sort()

# 음수 배열 처리
while len(m_arr) > 1:
    ans += hq.heappop(m_arr) * hq.heappop(m_arr)

# 음수 남음
if m_arr:
    # 음수 남고 0 있으면 곱하기
    if zero_cnt:
        ans += hq.heappop(m_arr) * 0
        zero_cnt -= 1

    # 음수 남고 0 없으면 더하기
    else:
        ans += m_arr[0]

# 양수 배열 처리
while len(p_arr) > 1:
    a = p_arr.pop()
    b = p_arr.pop()
    if a == 1 or b == 1:
        ans += a + b
    else:
        ans += a * b

# 양수 남음
if p_arr:
    # 더하기
    ans += p_arr.pop()

print(ans)
