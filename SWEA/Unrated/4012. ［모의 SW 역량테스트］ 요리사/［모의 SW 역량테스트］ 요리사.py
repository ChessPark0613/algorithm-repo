from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    food = range(N)
    ans = float("inf")
    for comb in combinations(food, N // 2):
        # 조합으로 뽑고
        food_a = set(comb)
        # 뽑은거 빼고 나머지
        food_b = set(food) - food_a


        taste_a = 0
        for y in food_a:
            for x in food_a:
                if y != x:
                    taste_a += S[y][x]

        taste_b = 0
        for y in food_b:
            for x in food_b:
                if y != x:
                    taste_b += S[y][x]

        ans = min(abs(taste_a - taste_b), ans)

    print(f"#{tc} {ans}")