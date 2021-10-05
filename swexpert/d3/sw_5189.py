# 전자카트
import math

test_cases = int(input().strip())


def dfs(x, depth, value):
    global result
    if depth == N - 1:
        result = min(value + mat[x][0], result)
        return
    if value > result:
        return
    for i in range(N):
        if not visited[i] and mat[x][i] != 0:
            visited[x] = True
            dfs(i, depth + 1, value + mat[x][i])
            visited[x] = False


for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [False] * N
    result = math.inf
    dfs(0, 0, 0)
    print('#{} {}'.format(t, result))
