
testCase = int(input().strip())

for i in range(1, testCase + 1):
    minimum, maximum, minutes = tuple(map(int, input().strip().split()))
    result = 0
    if minimum <= minutes <= maximum:
        result = 0
    elif minutes < minimum:
        result = minimum - minutes
    else:
        result = -1

    print('#{} {}'.format(i, result))
