def solve_case(arr):
    n = len(arr)
    dp = [[0]*(n) for _ in range(n)]

    for length in range(1, n+1):
        for l in range(0, n-length+1):
            r = l + length - 1

            best = 0
            for k in range(l, r+1):
                left  = dp[l][k-1] if k-1 >= l else 0
                right = dp[k+1][r] if k+1 <= r else 0

                if l == 0 and r == n-1:
                    gain = arr[k]
                elif l == 0 and r < n-1:
                    gain = arr[r+1]
                elif l > 0 and r == n-1:
                    gain = arr[l-1]
                else:
                    gain = arr[l-1] * arr[r+1]

                best = max(best, left + right + gain)

            dp[l][r] = best

    return dp[0][n-1]

if __name__ == "__main__":
    T = int(input().strip())
    for tc in range(1, T + 1):
        N = int(input().strip())
        nums = list(map(int, input().split()))
        print(f"#{tc} {solve_case(nums)}")
