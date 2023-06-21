import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    mat = [list(sys.stdin.readline().strip()) for _ in range(n)]

    white_checker_board = []
    black_checker_board = []
    for i in range(8):
        if i % 2 == 0:
            white_checker_board.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
            black_checker_board.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
        else:
            white_checker_board.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
            black_checker_board.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])

    result = 8 * 8
    for i in range(n - 7):
        for j in range(m - 7):
            white_checker_paint = 0
            black_checker_paint = 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if mat[k][l] != white_checker_board[k-i-1][l-j-1]:
                        white_checker_paint += 1
                    if mat[k][l] != black_checker_board[k-i-1][l-j-1]:
                        black_checker_paint += 1

            result = min(result, min(white_checker_paint, black_checker_paint))
    sys.stdout.write(str(result))