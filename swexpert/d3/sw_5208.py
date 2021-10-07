# 전기버스2
import math

test_cases = int(input().strip())


def recursion(idx, remain, swap):
    global cnt

    if swap >= cnt:
        return
    if remain == 0:
        return
    if idx >= N - 2:
        cnt = min(cnt, swap)
        return

    recursion(idx + 1, station[idx + 1], swap + 1)
    recursion(idx + 1, remain - 1, swap)


for t in range(1, test_cases + 1):
    nums = list(map(int, input().strip().split()))
    N = nums[0]
    station = nums[1:]
    cnt = math.inf
    recursion(0, station[0], 0)
    print('#{} {}'.format(t, cnt))

'''
def recursion(idx, swap):
    global cnt

    if swap >= cnt:
        return

    if idx >= N - 1:
        cnt = min(cnt, swap)
        return

    for i in range(station[idx]):
        recursion(idx + 1 + i, swap + 1)


for t in range(1, test_cases + 1):
    nums = list(map(int, input().strip().split()))
    N = nums[0]
    station = nums[1:]
    cnt = math.inf
    recursion(0, -1)
    print('#{} {}'.format(t, cnt))
'''
