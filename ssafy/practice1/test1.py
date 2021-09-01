test_cases = int(input().strip())

dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for t in range(1, test_cases + 1):
    n = int(input().strip())
    mat = [list(input().strip()) for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if mat[y][x] == 'A':
                for d in dxy:
                    tx, ty = x + d[0], y + d[1]
                    if 0 <= tx < n and 0 <= ty < n and mat[ty][tx] == 'H':
                        mat[ty][tx] = 'X'

            if mat[y][x] == 'B':
                for i in range(1, 3):
                    for d in dxy:
                        tx, ty = x + d[0] * i, y + d[1] * i
                        if 0 <= tx < n and 0 <= ty < n and mat[ty][tx] == 'H':
                            mat[ty][tx] = 'X'

            if mat[y][x] == 'C':
                for i in range(1, 4):
                    for d in dxy:
                        tx, ty = x + d[0] * i, y + d[1] * i
                        if 0 <= tx < n and 0 <= ty < n and mat[ty][tx] == 'H':
                            mat[ty][tx] = 'X'

    cnt = 0
    for y in range(n):
        for x in range(n):
            if mat[y][x] == 'H':
                cnt += 1

    print('#{} {}'.format(t, cnt))
