def recursion(depth, value):
    global result

    if result >= value:
        return

    if depth == N:
        result = max(result, value)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            recursion(depth + 1, value * mat[depth][i] / 100)
            visited[i] = False


test_cases = int(input())
for t in range(1, test_cases + 1):
    N = int(input())
    mat = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [False] * N
    result = 0
    recursion(0, 1)
    print('#{} {:.6f}'.format(t, result * 100))
