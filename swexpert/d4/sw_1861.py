# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def check():
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ty, tx = y + dy[i], x + dx[i]
                # 9 3 4
                # 6 1 5
                # 7 8 2
                if 0 <= ty < N and 0 <= tx < N and mat[ty][tx] == mat[y][x] + 1:
                    visited[mat[ty][tx]] = True
                # 0 1 2 3 4 5 6 7 8 9
                # F F F T T F T T F F


def solve():
    i = N * N  # 9
    room_num = 0
    max_room = 0
    v = 1
    # 0 1 2 3 4 5 6 7 8 9
    # F F F T T F T T F F
    while i >= 0:
        while visited[i]:
            v += 1
            i -= 1
        if max_room <= v:
            max_room = v
            room_num = i
        v = 1
        i -= 1
    return room_num, max_room


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N = int(input().strip())  # 3
    mat = [list(map(int, input().strip().split())) for _ in range(N)]
    # 0 1 2 3 4 5 6 7 8 9
    visited = [False] * (N * N + 1)
    check()
    num, room = solve()
    print('#{} {} {}'.format(t, num, room))
