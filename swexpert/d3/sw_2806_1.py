test_cases = int(input().strip())


def possible(pos, row):
    for r in range(row):
        if pos == rows[r] or abs(pos - rows[r]) == row - r:
            return False
    return True


def recursion(row):
    global result
    if row == N:
        result += 1

    for i in range(N):
        if possible(i, row):
            rows[row] = i
            recursion(row + 1)


for t in range(1, test_cases + 1):
    N = int(input().strip())
    rows = [0] * N
    result = 0
    recursion(0)
    print('#{} {}'.format(t, result))
