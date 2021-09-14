test_cases = int(input().strip())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


mat = [[0] * 301 for _ in range(301)]
x, y = 1, 1
number = 1
while y < 301:
    x, ty = 1, y
    while x <= y:
        if ty > 0:
            mat[ty][x] = number
            ty -= 1
            x += 1
            number += 1
    y += 1

for t in range(1, test_cases + 1):
    n, m = map(int, input().split())

    point1 = Point(0, 0)
    # point1 = [0, 0]
    point2 = Point(0, 0)
    for y in range(1, 301):
        for x in range(1, 301):
            if mat[y][x] == n:
                point1.x = x
                point1.y = y
                # point[0] = x
                # point[1] = y
            if mat[y][x] == m:
                point2.x = x
                point2.y = y
        if point1.x and point2.x:
            break

    # newPoint = [point1[0] + ... ... ... .. .. .. .. .. ..]
    newPoint = Point(point1.x + point2.x, point1.y + point2.y)
    result = mat[newPoint.y][newPoint.x]
    print('#{} {}'.format(t, result))
