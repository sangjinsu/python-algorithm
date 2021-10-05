# 컨테이너 운반
test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())
    weights = list(map(int, input().strip().split()))
    trucks = list(map(int, input().strip().split()))

    weights.sort(reverse=True)
    trucks.sort(reverse=True)

    result = 0
    i, j = 0, 0
    while i < N and j < M:
        if weights[i] <= trucks[j]:
            result += weights[i]
            i += 1
            j += 1
        else:
            i += 1
    print('#{} {}'.format(t, result))
