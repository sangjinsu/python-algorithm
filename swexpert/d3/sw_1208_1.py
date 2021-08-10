test_cases = 10

for t in range(1, test_cases + 1):
    n = int(input().strip())
    boxes = list(map(int, input().strip().split()))

    highest = 0
    lowest = 101
    for box in boxes:
        if highest < box:
            highest = box
        if lowest > box:
            lowest = box

    counts = [0] * (highest + 1)
    for box in boxes:
        counts[box] += 1

    i = 0
    while i < n and lowest < highest:
        counts[lowest] -= 1
        counts[lowest + 1] += 1

        counts[highest] -= 1
        counts[highest - 1] += 1

        if counts[lowest] == 0:
            lowest += 1
        if counts[highest] == 0:
            highest -= 1

        i += 1

    result = highest - lowest
    print('#{} {}'.format(t, result))
