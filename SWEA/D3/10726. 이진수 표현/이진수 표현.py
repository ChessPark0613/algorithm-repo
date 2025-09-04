def solve(n, m):
    lst = bin(m)
    start = len(lst) - 1
    end = start - n
    for a in range(start, end, -1):
        if lst[a] != "1":
            return False
    return True


if __name__ == "__main__":
    t = int(input())
    for tc in range(1, t + 1):
        n, m = map(int, input().split())
        ans = "ON" if solve(n, m) else "OFF"
        print(f"#{tc}", ans)

