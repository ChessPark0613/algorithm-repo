from collections import deque

def get_ma(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def hex_convert(line):
    s = line.strip()
    if not s:
        return None
    li = ''.join(format(int(ch, 16), '04b') for ch in s)
    if '1' in li:
        return li
    return None

# 8자리로 다시 변환
def decode(b, idx):
    c4 = c3 = c2 = c1 = 0

    while idx >= 0 and b[idx] == '1':
        c4 += 1
        idx -= 1
    while idx >= 0 and b[idx] == '0':
        c3 += 1
        idx -= 1
    while idx >= 0 and b[idx] == '1':
        c2 += 1
        idx -= 1
    while idx >= 0 and b[idx] == '0':
        c1 += 1
        idx -= 1

    if c2 == 0 or c3 == 0 or c4 == 0:
        return None, idx, None

    ma = get_ma(get_ma(c1, c2), get_ma(c3, c4))
    ratio = (c1 // ma, c2 // ma, c3 // ma, c4 // ma)

    digit = RATIO.get(ratio)
    if digit is None:
        return None, idx, ma

    return digit, idx, ma

def solve(lst):
    ans = 0
    for p_code in lst:
        even = 0
        odd = 0
        total = 0
        for i in range(8):
            v = int(p_code[i])
            total += v
            if i % 2 == 0:
                even += v
            else:
                odd += v
        if (even * 3 + odd) % 10 == 0:
            ans += total
    return ans

if __name__ == "__main__":
    RATIO = {
        (3, 2, 1, 1): 0,
        (2, 2, 2, 1): 1,
        (2, 1, 2, 2): 2,
        (1, 4, 1, 1): 3,
        (1, 1, 3, 2): 4,
        (1, 2, 3, 1): 5,
        (1, 1, 1, 4): 6,
        (1, 3, 1, 2): 7,
        (1, 2, 1, 3): 8,
        (3, 1, 1, 2): 9,
    }

    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        lines = [input().strip() for _ in range(N)]
        bins = {b for b in (hex_convert(line) for line in lines) if b is not None}
        lines = list(bins)

        pass_code = set()

        for row in lines:
            idx = M * 4 - 1
            while idx >= 0:
                if row[idx] == '0':
                    idx -= 1
                    continue

                # 8자리 복원 시도
                digits = deque()
                save_idx = idx
                last_ma = 1

                for _ in range(8):
                    digit, idx, ma = decode(row, idx)

                    if digit is None:
                        idx = save_idx - 1
                        digits.clear()
                        break

                    digits.appendleft(digit)
                    last_ma = ma if ma else last_ma

                    if len(digits) == 8:
                        c = ''.join(map(str, digits))
                        pass_code.add(c)
                        break

                    if len(digits) == 7:
                        if last_ma is None or last_ma == 0:
                            continue
                        span = 7 * last_ma
                        start = max(0, idx - span + 1)
                        x = row[start: idx + 1]

                        x1 = x2 = x3 = x4 = 0
                        p = len(x) - 1

                        while p >= 0 and x[p] == '1':
                            x4 += 1; p -= 1
                        while p >= 0 and x[p] == '0':
                            x3 += 1; p -= 1
                        while p >= 0 and x[p] == '1':
                            x2 += 1; p -= 1
                        while p >= 0 and x[p] == '0':
                            x1 += 1; p -= 1

                        if x2 and x3 and x4:
                            g = get_ma(get_ma(x1, x2), get_ma(x3, x4))
                            if g != 0:
                                ratio = (x1 // g, x2 // g, x3 // g, x4 // g)
                                d = RATIO.get(ratio)
                                if d is not None:
                                    digits.appendleft(d)
                                    c = ''.join(map(str, digits))
                                    pass_code.add(c)
                                    break

        res = solve(sorted(pass_code))
        print(f"#{tc} {res}")
