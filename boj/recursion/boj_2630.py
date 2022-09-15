import sys

blue = 0
white = 0


def recursion(y, x, size):
    global white, blue
    if is_same_color(y, x, size):
        if table[y][x]:
            blue += 1
        else:
            white += 1
        return

    half_size = size // 2
    recursion(y, x, half_size)
    recursion(y, x + half_size, half_size)
    recursion(y + half_size, x, half_size)
    recursion(y + half_size, x + half_size, half_size)


def is_same_color(y, x, size):
    color = table[y][x]
    for ty in range(y, y + size):
        for tx in range(x, x + size):
            if table[ty][tx] != color:
                return False
    return True


N = int(sys.stdin.readline().strip())
table = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
recursion(0, 0, N)

sys.stdout.write(str(white) + '\n')
sys.stdout.write(str(blue) + '\n')
