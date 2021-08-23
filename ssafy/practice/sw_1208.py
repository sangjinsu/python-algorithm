test_cases = 10

for t in range(1, test_cases + 1):
    dump = int(input().strip())
    boxes = list(map(int, input().strip().split()))

    h = 0
    l = 101
    for box in boxes:
        if box > h:
            h = box
        if box < l:
            l = box

    counts = [0] * (h + 1)
    for box in boxes:
        counts[box] += 1

    while dump > 0 and l < h:
        counts[h] -= 1
        counts[l] -= 1

        counts[h - 1] += 1
        counts[l + 1] += 1

        if counts[h] == 0:
            h -= 1
        if counts[l] == 0:
            l += 1
        dump -= 1
    result = h - l
    print('#{} {}'.format(t, result))
