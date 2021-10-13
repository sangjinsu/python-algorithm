# 요리사
import math


def recursion(idx, c):
    global result
    if c == N // 2:
        dish1 = list()
        dish2 = list()
        for i in range(len(visited)):
            if visited[i]:
                dish1.append(i)
            else:
                dish2.append(i)
        dish1_synergy = 0
        dish2_synergy = 0
        for i in dish1:
            for j in dish1:
                dish1_synergy += mat[i][j]
        for i in dish2:
            for j in dish2:
                dish2_synergy += mat[i][j]
        result = min(result, abs(dish1_synergy - dish2_synergy))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            recursion(i + 1, c + 1)
            visited[i] = False


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    visited = [False] * N
    mat = [list(map(int, input().strip().split())) for _ in range(N)]
    total = 0
    result = math.inf
    recursion(0, 0)
    print('#{} {}'.format(t, result))
