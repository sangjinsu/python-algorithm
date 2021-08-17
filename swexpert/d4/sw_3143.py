test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    a, b = input().strip().split()

    cnt = 0
    i = 0
    while i < len(a) - len(b) + 1:
        if a[i:i + len(b)] == b:
            cnt += 1
            i += len(b)
        else:
            i += 1

    result = len(a) - cnt * (len(b) - 1)
    print('#{} {}'.format(t, result))
