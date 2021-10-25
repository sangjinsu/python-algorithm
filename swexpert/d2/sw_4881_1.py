test_cases = int(input().strip())


def recursion(n, value):
    global result

    if value >= result:
        return

    if n == N:
        result = min(result, value)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            recursion(n + 1, value + mat[n][i])
            visited[i] = False


for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [False] * N
    result = 999999
    recursion(0, 0)
    print('#{} {}'.format(t, result))
