import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

total = 0


def recursion(s, i, depth):
    global total

    if depth >= 3:
        if total < s <= M:
            total = s
        return

    if i >= len(nums):
        return

    recursion(s + nums[i], i + 1, depth + 1)
    recursion(s, i + 1, depth)


recursion(0, 0, 0)

sys.stdout.write(str(total))
