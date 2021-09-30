test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())
    binary = bin(M)[2:].zfill(N)[-N:]
    result = 'ON'
    if '0' in binary:
        result = 'OFF'
    print('#{} {}'.format(t, result))
