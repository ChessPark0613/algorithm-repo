T = int(input())

base = ["ZRO", "ONE", "TWO", "THR", "FOR", 
         "FIV", "SIX", "SVN", "EGT", "NIN"]

def _find(a, b):
    return base.index(a) - base.index(b)

for _ in range(T):
    tc, n = input().split()
    n = int(n)
    arr = input().split()

    res = []

    for word in arr:
        inserted = False
        for i in range(len(res)):
            if _find(word, res[i]) < 0:
                res.insert(i, word)
                inserted = True
                break
        if not inserted:
            res.append(word)

    print(tc)
    print(*res)