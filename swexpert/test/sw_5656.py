import math
from copy import deepcopy
from pprint import pprint

# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def delete_brick(y, x, board):
    queue = [(y, x, board[y][x])]
    board[y][x] = 0
    while queue:
        ny, nx, c = queue.pop(0)
        for i in range(c):
            for j in range(4):
                ty, tx = ny + dy[j] * i, nx + dx[j] * i
                if 0 <= ty < H and 0 <= tx < W:
                    if board[ty][tx]:
                        queue.append((ty, tx, board[ty][tx]))
                    board[ty][tx] = 0


def organize_brick(board):
    for i in range(W):
        queue = []
        cnt = 0
        for j in range(H - 1, -1, -1):
            if board[j][i]:
                queue.append(board[j][i])
                cnt += 1
        for j in range(H - 1, -1, -1):
            if queue:
                board[j][i] = queue.pop(0)
            else:
                board[j][i] = 0


def recursion(k, board):
    global min_cnt
    if k == N:
        cnt = 0
        for i in range(W):
            for j in range(H):
                if board[j][i]:
                    cnt += 1
            if cnt >= min_cnt:
                return
        # print(cnt)
        # pprint(board)
        min_cnt = min(min_cnt, cnt)
        return
    for i in range(W):
        for j in range(H):
            if board[j][i]:
                temp = deepcopy(board)
                delete_brick(j, i, temp)
                organize_brick(temp)
                recursion(k + 1, temp)
                break


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, W, H = map(int, input().strip().split())
    mat = [list(map(int, input().strip().split())) for _ in range(H)]
    min_cnt = math.inf
    recursion(0, mat)
    if min_cnt == math.inf:
        min_cnt = 0
    print('#{} {}'.format(t, min_cnt))
