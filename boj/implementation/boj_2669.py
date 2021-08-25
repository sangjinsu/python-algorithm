import sys

pointers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(4)]

plane = [[0] * 101 for _ in range(101)]

for pointer in pointers:
    x1, y1, x2, y2 = pointer
    for y in range(y1, y2):
        for x in range(x1, x2):
            plane[y][x] = 1

result = 0
for i in range(101):
    for j in range(101):
        result += plane[i][j]

sys.stdout.write(str(result))

