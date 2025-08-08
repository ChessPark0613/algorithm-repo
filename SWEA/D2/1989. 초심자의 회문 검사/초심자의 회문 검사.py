T = int(input())

for test_case in range(1, T + 1):
    str = list(input())
    M = len(str)
    pos = 0
    is_palindrome = True

    while M // 2 > pos:
        if str[pos] != str[M - 1 - pos]:
            is_palindrome = False

        pos += 1

    print(f"#{test_case}", int(is_palindrome))

