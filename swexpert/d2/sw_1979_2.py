test_cases = int(input())

for t in range(1, test_cases + 1):
    n, k = map(int, input().strip().split())
    puzzle = [list(map(int, input().strip().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        row = 0
        col = 0
        for j in range(n):
            if puzzle[i][j]:
                row += 1
            else:
                if row == k:
                    cnt += 1
                row = 0

            if puzzle[j][i]:
                col += 1
            else:
                if col == k:
                    cnt += 1
                col = 0

        if row == k:
            cnt += 1
        if col == k:
            cnt += 1

    print('#{} {}'.format(t, cnt))
