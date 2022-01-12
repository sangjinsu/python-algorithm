import sys

sys.setrecursionlimit(1500 * 1500)


def recursion(x, y):
    global total
    if check[x][y]:
        return
    check[x][y] = True
    a = [x, y, total - x - y]
    for i in range(3):
        for j in range(3):
            if a[i] < a[j]:
                b = [x, y, total - x - y]
                b[i] += a[i]
                b[j] -= a[i]
                recursion(b[0], b[1])


check = [[False] * 1501 for _ in range(1501)]
x, y, z = map(int, input().split())
total = x + y + z

if total % 3 != 0:
    sys.stdout.write(str(0))
else:
    recursion(x, y)
    if check[total // 3][total // 3]:
        sys.stdout.write(str(1))
    else:
        sys.stdout.write(str(0))
