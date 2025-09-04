def solve():
    max_cnt = n * m
    for i in range(1, n - 1):
        for j in range(i, n):
            if i == j:
                continue
            cnt = get_count(i, j)
            if cnt < max_cnt:
                max_cnt = cnt

    return max_cnt


def get_count(s1, s2) -> int:
    cw = cb = cr = 0
    white = base[:s1]
    blue = base[s1:s2]
    red = base[s2:]

    for w in white:
        cw += sum(1 for x in w if x != "W")
    for b in blue:
        cb += sum(1 for x in b if x != "B")
    for r in red:
        cr += sum(1 for x in r if x != "R")

    return cw + cb + cr


if __name__ == "__main__":
    t = int(input())

    for tc in range(1, t + 1):
        n, m = map(int, input().split())
        base = [list(map(str, input().strip())) for _ in range(n)]

        print(f"#{tc}", solve())
