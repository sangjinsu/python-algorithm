# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
tunnel = {
    1: [0, 1, 2, 3],
    2: [1, 3],
    3: [0, 2],
    4: [0, 3],
    5: [0, 1],
    6: [1, 2],
    7: [2, 3]
}


def bfs(x, y):
    result = 1
    queue = [[x, y]]
    isTunnel = [mat[y][x]]
    cnt = 0
    mat[y][x] = -1
    while queue and cnt < L - 1:
        queueLen = len(queue)
        for _ in range(queueLen):
            nx, ny = queue.pop(0)
            t = isTunnel.pop(0)

            for move in tunnel[t]:
                tx, ty = nx + dx[move], ny + dy[move]
                if 0 <= tx < M and 0 <= ty < N and mat[ty][tx] > 0:
                    if (move + 2) % 4 in tunnel[mat[ty][tx]]:
                        queue.append([tx, ty])
                        isTunnel.append(mat[ty][tx])
                        mat[ty][tx] = -1
                        result += 1
        cnt += 1
    return result


test_cases = int(input())
for t in range(1, test_cases + 1):
    N, M, R, C, L = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = bfs(C, R)
    print('#{} {}'.format(t, result))
