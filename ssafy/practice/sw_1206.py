test_cases = 10


def max_bd(bds):
    m = 0
    for bd in bds:
        if m < bd:
            m = bd
    return m


for t in range(1, test_cases + 1):
    test_num = int(input())
    bds = list(map(int, input().strip().split()))
    result = 0
    for i in range(2, len(bds) - 2):
        hd = max_bd([bds[i - 2], bds[i - 1], bds[i + 1], bds[i + 2]])
        if bds[i] > hd:
            result += bds[i] - hd
    print('#{} {}'.format(t, result))
