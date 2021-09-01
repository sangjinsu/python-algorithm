test_cases = int(input())

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, test_cases + 1):
    m, d = map(int, input().split())
    result = (sum(month[:m]) + 3 + d) % 7
    print('#{} {}'.format(t, result))
