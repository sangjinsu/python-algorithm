# 화물 도크
test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N = int(input().strip())
    lines = [tuple(map(int, input().strip().split())) for _ in range(N)]
    lines.sort(key=lambda x: (x[1], x[0]))

    cnt = 1
    end = lines[0][1]
    for i in range(1, N):
        if lines[i][0] >= end:
            cnt += 1
            end = lines[i][1]

    print('#{} {}'.format(t, cnt))
