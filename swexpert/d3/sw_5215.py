test_cases = int(input().strip())


def recursion(idx, h, c):
    global happy

    if c > L:
        return

    if idx >= N:
        happy = max(happy, h)
        return

    calorie = c + ingredients[idx][1]
    if calorie < L:
        recursion(idx + 1, h + ingredients[idx][0], calorie)
    recursion(idx + 1, h, c)


for t in range(1, test_cases + 1):
    N, L = map(int, input().strip().split())
    ingredients = [tuple(map(int, input().strip().split())) for _ in range(N)]
    happy = -1
    recursion(0, 0, 0)
    print('#{} {}'.format(t, happy))
