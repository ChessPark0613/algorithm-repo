def solve(n):
    cnt = 0
    ans = ""

    while n > 0 and cnt < 13:
        n = n * 2
        if n >= 1:
            ans += "1"
            n -= 1
        else:
            ans += "0"

        cnt += 1

    if cnt == 13:
        ans = "overflow"

    print(f"#{tc} {ans}")


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = float(input().strip())
        solve(N)
