def make_set(n):
    return [x for x in range(n + 1)]


def find_set(x):
    # x의 대표자를 반환
    if x == parent[x]:
        return x
    return find_set(parent[x])


def union(x, y):
    px = find_set(x)
    py = find_set(y)
    # 서로 다른 집합일 때, 한 집합의 대표의 부모를 다른 집합의 대표로 변경
    if px != py:
        parent[py] = px


parent = []

T = int(input())
for tc in range(1, T + 1):
    # N은 학생수, M은 신청서 수
    N, M = map(int, input().split())
    # 신청서 M장의 정보, 신청서 한 장당 숫자 2개
    data = list(map(int, input().split()))
    # N 명의 학생에 대해서 서로소 집합 만들기
    parent = make_set(N)
    # 신청서 읽기
    for i in range(0, M * 2, 2):
        # data[i]번 학생과 data[i+1]번 학생 같은조 만들기
        union(data[i], data[i + 1])

    # 몇 개의 조가 만들어졌는지 확인
    group = set()  # 그룹 대표자의 개수가 그룹의 개수
    for i in range(1, N + 1):
        # 모든 학생이 속한 그룹의 대표자를 set에 넣기
        group.add(find_set(i))

    print(f'#{tc} {len(group)}')