from itertools import combinations


def find_num(cnt):
    global max_num

    if cnt >= swap:
        max_num = max(max_num, int(''.join(nums)))
        return

    for i, j in comb:
        nums[i], nums[j] = nums[j], nums[i]
        temp = ''.join(nums)
        if (temp, cnt + 1) not in visited:
            visited.add((temp, cnt + 1))
            find_num(cnt + 1)
        nums[i], nums[j] = nums[j], nums[i]


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    nums, swap = input().strip().split()

    max_num = -1
    visited = set()
    nums = list(nums)
    swap = int(swap)
    nums_len = len(nums)

    comb = list(combinations([i for i in range(nums_len)], 2))

    find_num(0)

    print('#{} {}'.format(t, max_num))
