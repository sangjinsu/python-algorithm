test_cases = int(input())

for t in range(1, test_cases + 1):
    D, A, B, F = map(int, input().strip().split())
    print('#{} {}'.format(t, D / (A + B) * F))
