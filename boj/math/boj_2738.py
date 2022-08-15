import sys

N, M = map(int, sys.stdin.readline().strip().split())

mat_1 = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
mat_2 = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for y in range(N):
    for x in range(M):
        mat_1[y][x] += mat_2[y][x]

for nums in mat_1:
    print(*nums)
