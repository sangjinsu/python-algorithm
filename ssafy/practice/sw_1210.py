test_cases = 10
for t in range(1, test_cases + 1):
    test_num = int(input())
    mat = [list(map(int, input().strip().split())) for _ in range(100)]

    end = -1
    for i in range(100):
        if mat[99][i] == 2:
            end = i
            break

    nx = end
    ny = 99

    while ny > 0:
        ny -= 1
        if 0 <= nx - 1 and mat[ny][nx - 1] == 1:
            while 0 <= nx - 1 and mat[ny][nx - 1] == 1:
                nx -= 1
        elif nx + 1 < 100 and mat[ny][nx + 1] == 1:
            while nx + 1 < 100 and mat[ny][nx + 1] == 1:
                nx += 1

    print('#{} {}'.format(t, nx))
