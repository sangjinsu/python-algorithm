import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().strip().split())
nums = [*map(int, sys.stdin.readline().strip().split())]

cnt = 0


# 비트 연산자 사용
# for i in range(1, 1 << len(nums)):
#     total = 0
#     for j in range(len(nums) + 1):
#         print(i & (1 << j))
#         if i & (1 << j):
#
#             print(nums[j], end=' ')
#             total += nums[j]
#     print()
#     if total == s:
#         cnt += 1

# itertools combinations 사용
for i in range(1, n + 1):
    combs = combinations(nums, i)
    for comb in combs:
        if sum(comb) == s:
            cnt += 1

# 재귀 사용
# def subset(index, total):
#     global cnt
#     if index == n:
#         return
# 
#     if total + nums[index] == s:
#         cnt += 1
# 
#     subset(index + 1, total)
#     subset(index + 1, total + nums[index])

# subset(0, 0)

sys.stdout.write(str(cnt))
