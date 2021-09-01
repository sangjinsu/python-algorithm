test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n, m, k = tuple(map(int, input().strip().split()))
    persons = list(map(int, input().strip().split()))
    persons.sort()
    result = 1
    cnt = 1
    for p in persons:
        fish = (p // m) * k
        if fish - cnt < 0:
            result = 0
            break
        else:
            cnt += 1

    if result:
        print('#{} Possible'.format(t))
    else:
        print('#{} Impossible'.format(t))
