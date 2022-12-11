import pprint
import sys

N, M = map(int, sys.stdin.readline().strip().split())
mat = [[0] * (N + 1) for _ in range(N + 1)]
smat = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    line = [0] + list(map(int, sys.stdin.readline().strip().split()))
    mat[i + 1] = line

for y in range(1, N + 1):
    for x in range(1, N + 1):
        smat[y][x] = -smat[y - 1][x - 1] + mat[y][x] + smat[y - 1][x] + smat[y][x - 1]

pprint.pprint(smat)

for i in range(M):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().strip().split())
    result = smat[y2][x2] - smat[y2][x1 - 1] - smat[y1 - 1][x2] + smat[y1 - 1][x1 - 1]
    sys.stdout.write(str(result) + '\n')
