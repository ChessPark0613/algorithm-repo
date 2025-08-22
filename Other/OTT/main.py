# main.py
# 채점 시스템 구동용. 필요 시 sample_input.txt 리다이렉션 주석 해제.
# import sys
# sys.stdin = open("res/sample_input.txt", "r", encoding="utf-8")
# https://swexpertacademy.com/main/code/codeBattle/problemDetail.do

import sys
from solution import UserSolution, RESULT

CMD_INIT = 100
CMD_ADD = 200
CMD_ERASE = 300
CMD_WATCH = 400
CMD_SUGGEST = 500


def run(it) -> bool:
    usersolution = UserSolution()

    def next_int():
        return int(next(it))

    Q = next_int()
    okay = False

    for _ in range(Q):
        cmd = next_int()

        if cmd == CMD_INIT:
            N = next_int()
            usersolution.init(N)
            okay = True

        elif cmd == CMD_ADD:
            mID = next_int()
            mGenre = next_int()
            mTotal = next_int()
            ret = usersolution.add(mID, mGenre, mTotal)
            ans = next_int()
            if ret != ans:
                okay = False

        elif cmd == CMD_ERASE:
            mID = next_int()
            ret = usersolution.erase(mID)
            ans = next_int()
            if ret != ans:
                okay = False

        elif cmd == CMD_WATCH:
            uID = next_int()
            mID = next_int()
            mRating = next_int()
            ret = usersolution.watch(uID, mID, mRating)
            ans = next_int()
            if ret != ans:
                okay = False

        elif cmd == CMD_SUGGEST:
            uID = next_int()
            res: RESULT = usersolution.suggest(uID)
            cnt = next_int()
            if res.cnt != cnt:
                okay = False
            for i in range(cnt):
                ans = next_int()
                if res.IDs[i] != ans:
                    okay = False
        else:
            okay = False

    return okay


def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)

    TC = int(next(it))
    MARK = int(next(it))

    out_lines = []
    for tc in range(1, TC + 1):
        score = MARK if run(it) else 0
        out_lines.append(f"#{tc} {score}")
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
