test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    a, b, c = map(int, input().strip().split())
    print('#{} {}'.format(t, c // min(a, b)))
