test_cases = int(input())

for t in range(1, test_cases + 1):
    sides = {}
    for side in list(input().strip().split()):
        sides.setdefault(side, 0)
        sides[side] += 1

    result = 0
    for i, side in sides.items():
        if side != 2:
            result = i

    print('#{} {}'.format(t, result))