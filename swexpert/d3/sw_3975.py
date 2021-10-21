test_cases = int(input().strip())

results = [''] * (test_cases + 1)
for t in range(1, test_cases + 1):
    A, B, C, D = map(int, input().strip().split())
    k = A * D - C * B
    result = 'DRAW'
    if k > 0:
        result = 'ALICE'
    elif k < 0:
        result = 'BOB'
    results[t] = result

for i in range(1, test_cases + 1):
    print('#{} {}'.format(i, results[i]))
