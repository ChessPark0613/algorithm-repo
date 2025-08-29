T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * (N + 1)
    val = 1

    def tq(i: int):
        global val
        if i > N:
            return
        tq(i * 2)
        arr[i] = val
        val += 1
        tq(i * 2 + 1)

    tq(1)
    print(f"#{tc} {arr[1]} {arr[N // 2]}")