N = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr.reverse()
ans = 0

for i, m in enumerate(arr):
    ans += sum(arr[i:])

print(ans)