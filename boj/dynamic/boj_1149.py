N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

for y in range(1, N):
    mat[y][0] += min(mat[y - 1][1], mat[y - 1][2])
    mat[y][1] += min(mat[y - 1][0], mat[y - 1][2])
    mat[y][2] += min(mat[y - 1][0], mat[y - 1][1])

print(min(mat[N - 1]))
