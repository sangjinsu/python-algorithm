test_cases = int(input().strip())

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

command = {
    'U': ('^', 0),
    'D': ('v', 2),
    'L': ('<', 3),
    'R': ('>', 1),
    '^': 0,
    'v': 2,
    '<': 3,
    '>': 1,
}

for t in range(1, test_cases + 1):
    H, W = map(int, input().strip().split())
    mat = [list(input().strip()) for _ in range(H)]

    N = int(input().strip())
    moves = input().strip()

    ny, nx = -1, -1
    for y in range(H):
        for x in range(W):
            if mat[y][x] in '^v<>':
                ny, nx = y, x

    for move in moves:
        if move in 'UDLR':
            mat[ny][nx] = command[move][0]
            direction = command[move][1]
            ty, tx = ny + dy[direction], nx + dx[direction]
            if 0 <= ty < H and 0 <= tx < W and mat[ty][tx] == '.':
                mat[ny][nx] = '.'
                mat[ty][tx] = command[move][0]
                ny, nx = ty, tx
        else:
            ky, kx = ny, nx
            direction = command[mat[ny][nx]]
            ky, kx = ky + dy[direction], kx + dx[direction]
            while 0 <= ky < H and 0 <= kx < W:
                if mat[ky][kx] == '*':
                    mat[ky][kx] = '.'
                    break
                if mat[ky][kx] == '#':
                    break
                ky, kx = ky + dy[direction], kx + dx[direction]

    print('#{}'.format(t), end=' ')
    for i in range(len(mat)):
        print(''.join(mat[i]))
