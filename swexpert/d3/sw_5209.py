# 최소 생산 비용
import math


def recursion(depth, value):
    global total

    if total < value:
        return

    if depth == N:
        total = min(total, value)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            recursion(depth + 1, value + mat[depth][i])
            visited[i] = False


test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [list(map(int, input().strip().split())) for _ in range(N)]
    total = math.inf
    visited = [False] * N
    recursion(0, 0)
    print('#{} {}'.format(t, total))
