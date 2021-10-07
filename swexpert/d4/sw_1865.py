# 동철이의 일 분배
def recursion(depth, value):
    global possible
    if possible >= value:
        return

    if depth == N:
        possible = max(possible, value)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            recursion(depth + 1, value * mat[depth][i] / 100)
            visited[i] = False


test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [list(map(int, input().strip().split())) for _ in range(N)]
    possible = 0
    visited = [False] * N
    recursion(0, 1)
    possible *= 100
    print('#{} {:.6f}'.format(t, possible))
