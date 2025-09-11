N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
chk = [0] * (d + 1)
tmp = 0

for i in range(k):
    if chk[belt[i]] == 0:
        tmp += 1
    chk[belt[i]] += 1

ans = tmp + (1 if chk[c] == 0 else 0)

for i in range(0, N):
    left = belt[i]
    chk[left] -= 1
    if chk[left] == 0:
        tmp -= 1

    right = belt[(i + k) % N]
    if chk[right] == 0:
        tmp += 1
    chk[right] += 1

    ans = max(ans, tmp + (1 if chk[c] == 0 else 0))

print(ans)