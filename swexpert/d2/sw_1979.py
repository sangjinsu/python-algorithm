test_cases = int(input())


def find_space(puzzle, n, k, axis='row'):
    cnt = 0
    if axis == 'row':
        for i in range(n):
            space = 0
            for j in range(n):
                if puzzle[i][j]:
                    space += 1
                else:
                    if space == k:
                        cnt += 1
                    space = 0

            if space == k:
                cnt += 1
    elif axis == 'col':
        for i in range(n):
            space = 0
            for j in range(n):
                if puzzle[j][i]:
                    space += 1
                else:
                    if space == k:
                        cnt += 1
                    space = 0

            if space == k:
                cnt += 1
    return cnt


for t in range(1, test_cases + 1):
    n, k = map(int, input().strip().split())
    puzzle = [list(map(int, input().strip().split())) for _ in range(n)]

    cnt = 0
    cnt += find_space(puzzle, n, k, axis='row')
    cnt += find_space(puzzle, n, k, axis='col')

    print('#{} {}'.format(t, cnt))
