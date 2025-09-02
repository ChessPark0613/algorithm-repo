def solve(n, hex):
    tmp = ""
    for i in range(n):
        tmp += book.get(hex[i])
    print(f"#{tc} {tmp}")


if __name__ == "__main__":
    T = int(input())

    book = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    for tc in range(1, T + 1):
        N, HEX = map(str, input().split())

        solve(int(N), HEX)
