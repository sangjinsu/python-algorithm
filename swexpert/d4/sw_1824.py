from collections import deque

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

direction = {'^': 0, 'v': 1, '<': 2, '>': 3}


def solve():
    Q = deque()
    visited = set()

    Q.append((0, 0, 0, 3))
    visited.add((0, 0, 0, 3))

    while Q:
        ny, nx, mem, dr = Q.popleft()
        mark = mat[ny][nx]

        # 상 하 좌 우
        if mark == '@':
            return 'YES'
        elif mark in '^v><':
            dr = direction[mark]
        elif mark == '_':
            if mem == 0:
                dr = 3
            else:
                dr = 2
        elif mark == '|':
            if mem == 0:
                dr = 1
            else:
                dr = 0
        elif '0' <= mark <= '9':
            mem = int(mark)
        elif mark == '+':
            mem = (mem + 1) % 16
        elif mark == '-':
            mem = (mem - 1) % 16
        elif mark == '?':
            for i in range(4):
                ty = (ny + dy[i]) % R
                tx = (nx + dx[i]) % C
                if (ty, tx, mem, i) not in visited:
                    Q.append((ty, tx, mem, i))
                    visited.add((ty, tx, mem, i))
            continue

        ty = (ny + dy[dr]) % R
        tx = (nx + dx[dr]) % C
        if (ty, tx, mem, dr) not in visited:
            Q.append((ty, tx, mem, dr))
            visited.add((ty, tx, mem, dr))

    return 'NO'


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    R, C = map(int, input().strip().split())
    mat = [input().strip() for _ in range(R)]
    result = solve()
    print('#{} {}'.format(t, result))
