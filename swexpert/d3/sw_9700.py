test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    p, q = map(float, input().strip().split())
    s1 = (1-p) * q
    s2 = p * (1-q) * q
    result = 'YES' if s1 < s2 else 'NO'
    print('#{} {}'.format(t, result))