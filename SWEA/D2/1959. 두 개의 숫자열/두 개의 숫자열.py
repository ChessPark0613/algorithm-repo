if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        if M >= N:
            arr1 = list(map(int, input().split()))
            arr2 = list(map(int, input().split()))
        else:
            N, M = M, N
            arr2 = list(map(int, input().split()))
            arr1 = list(map(int, input().split()))

        res = 0

        for m in range(M - N + 1):
            s = 0
            for n in range(N):
                s += arr2[m+n] * arr1[n]

            res = max(res, s)

        print(f"#{tc} {res}")