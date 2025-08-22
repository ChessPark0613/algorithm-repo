# Hosper's Hack.py
def gosper_masks(n: int, k: int):
    if not (0 <= k <= n):
        return
    if k == 0:
        yield 0; return
    s = (1 << k) - 1
    limit = 1 << n
    while s < limit:
        yield s
        c = s & -s
        r = s + c
        s = (((r ^ s) >> 2) // c) | r


def choose_from_mask(base, mask: int):
    out = []
    i, m = 0, mask
    while m:
        if m & 1:
            out.append(base[i])
        i += 1
        m >>= 1
    return out


if __name__ == "__main__":
    # n, k = 6, 3
    # for m in gosper_masks(n, k):
    #     picked = [i + 1 for i in range(n) if (m >> i) & 1]
    #     print(f"{m:0{n}b}", picked)
    n, m = map(int, input().split())
    base = sorted(list(map(int, input().split())))
    for m in gosper_masks(n, m):
        combo = choose_from_mask(base, m)
        print(combo)
