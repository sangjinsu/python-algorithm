test_cases = int(input())


def find_space(n, axis='row'):
    cnt = 0
    if axis == 'row':
        for i in range(n):
            space = 0
            for j in range(n):
                box = puzzle[i][j]
                if box:
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
                box = puzzle[j][i]
                if box:
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
    puzzle = []
    for i in range(n):
        line = list(map(int, input().strip().split()))
        puzzle.append(line)

    cnt = 0
    cnt += find_space(n, axis='row')
    cnt += find_space(n, axis='col')

    print('#{} {}'.format(t, cnt))
