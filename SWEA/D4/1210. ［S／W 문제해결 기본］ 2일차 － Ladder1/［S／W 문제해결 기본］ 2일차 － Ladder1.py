for _ in range(10):
    test_case = int(input())
    base = [list(map(int, input().split())) for _ in range(100)]

    dy = [0, 0, -1]
    dx = [-1, 1, 0]

    pos_y = 0
    pos_x = 0
    prev_move = 0  # 0: 왼 1: 오 2: 위

    for x in range(100):
        if base[99][x] == 2:
            pos_x = x
            pos_y = 99
            break

    while pos_y:
        if pos_x > 0 and prev_move != 1 and base[pos_y][pos_x - 1] == 1:
            pos_x -= 1
            prev_move = 0
        elif pos_x < 99 and prev_move != 0 and base[pos_y][pos_x + 1] == 1:
            pos_x += 1
            prev_move = 1
        else:
            pos_y -= 1
            prev_move = 2

    print(f"#{test_case} {pos_x}")
