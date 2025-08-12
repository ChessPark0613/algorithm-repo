T = int(input())

for test_case in range(1, T + 1):
    day, month, three_month, year = map(int, input().split())
    base = list(map(int, input().split()))

    def find(cost_day, cost_month, cost_3month, cost_year, cal):
        dp = [0] * 13

        for m in range(1, 13):
            pay_day = dp[m - 1] + cost_day * cal[m - 1]
            pay_month = dp[m - 1] + cost_month
            dp[m] = min(pay_day, pay_month)

            prev = max(0, m - 3)
            dp[m] = min(dp[m], dp[prev] + cost_3month)

        return min(dp[12], cost_year)

    print(f"#{test_case}", find(day, month, three_month, year, base))