def solve(c, pw):
    ans, even, odd = 0, 0, 0
    for p in range(0, 8):
        if p % 2 == 0:
            even += pw[p]
        else:
            odd += pw[p]

    if (even * 3 + odd) % 10 == 0:
        ans = even + odd

    print(f"#{c} {ans}")


def get_code(l, pw):
    res_code = []
    for m in range(l - 7):
        c = "".join(map(str, pw[m:m + 7]))
        if c in pw_code and len(res_code) != 8:
            for x in range(m, m + 56, 7):
                p_code = "".join(map(str, pw[x:x + 7]))
                if pw_code.get(p_code) is None:
                    res_code.clear()
                    break
                else:
                    res_code.append(pw_code.get(p_code))
    return res_code


if __name__ == "__main__":
    pw_code = {
        "0001101": 0,
        "0011001": 1,
        "0010011": 2,
        "0111101": 3,
        "0100011": 4,
        "0110001": 5,
        "0101111": 6,
        "0111011": 7,
        "0110111": 8,
        "0001011": 9
    }

    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        tmp = [list(map(int, input().strip())) for _ in range(N)]
        raw_code = []
        for t in tmp:
            if all(x == 0 for x in t):
                continue
            raw_code.extend(t)
            break

        pass_code = get_code(M, raw_code)
        solve(tc, pass_code)
