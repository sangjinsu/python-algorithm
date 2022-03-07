def solution(triangle):
    for y in range(1, len(triangle)):
        for x in range(len(triangle[y])):
            if x == 0:
                triangle[y][x] += triangle[y - 1][x]
            elif x == len(triangle[y]) - 1:
                triangle[y][x] += triangle[y - 1][-1]
            else:
                triangle[y][x] = max(triangle[y][x] + triangle[y - 1][x], triangle[y][x] + triangle[y - 1][x - 1])

    return max(triangle[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
