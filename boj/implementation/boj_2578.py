mat = [list(map(int, input().split())) for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]


cnt = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        n = num[i][j]
        for y in range(5):
            for x in range(5):
                if mat[y][x] == n:
                    mat[y][x] = 0
                    break
        bingo = 0
        r_cross = True
        l_cross = True
        for y in range(5):
            row = True
            col = True
            for x in range(5):
                if mat[y][x] > 0:
                    row = False
                if mat[x][y] > 0:
                    col = False
                if x == y and mat[y][x] > 0:
                    r_cross = False
                if x == 4 - y and mat[y][x] > 0:
                    l_cross = False
            if row:
                bingo += 1
            if col:
                bingo += 1

        if r_cross:
            bingo += 1
        if l_cross:
            bingo += 1

        if bingo >= 3:
            break


