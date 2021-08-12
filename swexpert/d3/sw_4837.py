# 부분집합의 합

# from itertools import combinations
# test_cases = int(input().strip())
#
# nums = [i for i in range(1, 13)]
# for t in range(1, test_cases + 1):
#     n, k = map(int, input().strip().split())
#
#     cnt = 0
#     for comb in combinations(nums, n):
#         if sum(comb) == k:
#             cnt += 1
#
#     print('#{} {}'.format(t, cnt))


test_cases = int(input().strip())

nums = [i for i in range(1, 13)]
for t in range(1, test_cases + 1):
    n, k = map(int, input().strip().split())

    cnt = 0
    for i in range(1, 1 << len(nums)):
        total = 0
        num_cnt = 0
        for j in range(len(nums) + 1):
            if i & (1 << j):
                total += nums[j]
                num_cnt += 1
        if num_cnt == n and total == k:
            cnt += 1

    print('#{} {}'.format(t, cnt))
