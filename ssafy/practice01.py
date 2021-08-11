test_cases = int(input().strip())

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, test_cases + 1):
    n = int(input().strip())
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        nums = list(map(int, input().strip().split()))
        for j in range(n):
            matrix[i][j] = nums[j]

    total = 0
    for i in range(n):
        for j in range(n):
            subtotal = 0
            for k in range(4):
                nx = dx[k] + j
                ny = dy[k] + i

                if 0 <= nx < n and 0 <= ny < n:
                    subtotal += abs(matrix[i][j] - matrix[ny][nx])

            total += subtotal

    print('#{} {}'.format(t, total))



