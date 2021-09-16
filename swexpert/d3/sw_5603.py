test_cases = int(input())

for t in range(1, test_cases + 1):
    n = int(input())
    mow = sorted([int(input()) for _ in range(n)], reverse=True)
    avg = sum(mow) // n

    result = 0
    i = 0
    while mow[i] > avg:
        result += mow[i] - avg
        i += 1

    print('#{} {}'.format(t, result))
