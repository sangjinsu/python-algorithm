test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    h1, m1, h2, m2 = tuple(map(int, input().strip().split()))

    m = m1 + m2
    if m >= 60:
        m -= 60
        h1 += 1

    h = h1 + h2
    if h > 12:
        h -= 12

    print('#{} {} {}'.format(t, h, m))
