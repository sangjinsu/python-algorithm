import math


def recursion(idx, total):
    global top_height

    if top_height >= total >= B:
        top_height = min(top_height, total)
        return

    if idx == N:
        return

    recursion(idx + 1, total)
    recursion(idx + 1, total + heights[idx])


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, B = map(int, input().strip().split())
    heights = list(map(int, input().strip().split()))
    top_height = math.inf
    recursion(0, 0)
    result = top_height - B
    print('#{} {}'.format(t, result))
