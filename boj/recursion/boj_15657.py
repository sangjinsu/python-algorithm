def recursion(depth, value):
    if depth == M:
        print(*value)
        return
    for i in range(N):
        if value[-1] <= nums[i]:
            value.append(nums[i])
            recursion(depth + 1, value)
            value.pop()


N, M = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

for i in range(N):
    recursion(1, [nums[i]])
