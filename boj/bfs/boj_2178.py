import pprint
import sys
from collections import deque

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(y: int, x: int, n: int, m: int, mat: list[list[int]]):
    queue = deque([(y, x)])
    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < n and 0 <= tx < m and mat[ty][tx] == 1:
                mat[ty][tx] = mat[ny][nx] + 1
                queue.append((ty, tx))


def main():
    n, m = map(int, sys.stdin.readline().split())
    mat = list()
    for _ in range(n):
        mat.append(list(map(int, list(sys.stdin.readline().strip()))))
    start_x, start_y = (0, 0)
    bfs(start_y, start_x, n, m, mat)
    sys.stdout.write(str(mat[n-1][m-1]))


if __name__ == "__main__":
    main()
