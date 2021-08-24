# 배열 최소 합
test_cases = int(input().strip())


def find_min(k, n, tot, min_tot):
    if tot >= min_tot[0]:
        return

    if k == n:
        if min_tot[0] > tot:
            min_tot[0] = tot

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            find_min(k + 1, n, tot + mat[k][i], min_tot)
            visited[i] = False


for t in range(1, test_cases + 1):
    n = int(input().strip())
    mat = [list(map(int, input().strip().split())) for _ in range(n)]
    visited = [False] * n
    min_tot = [99999]
    find_min(0, n, 0, min_tot)
    print('#{} {}'.format(t, min_tot[0]))
