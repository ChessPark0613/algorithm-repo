T = int(input())

for test_case in range(1, T + 1):
    t, length = map(str, input().split())
    base = list(map(str, input().split()))
    res = []

    base_dic = {
        "ZRO": 0,
        "ONE": 0,
        "TWO": 0,
        "THR": 0,
        "FOR": 0,
        "FIV": 0,
        "SIX": 0,
        "SVN": 0,
        "EGT": 0,
        "NIN": 0
    }

    for b in base:
        num = base_dic.get(b) + 1
        base_dic.update({b: num})

    print(t)
    tmp = []
    for d in base_dic:
        tmp.extend([d] * base_dic.get(d))

    print(*tmp)
