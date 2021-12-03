def recursion(idx, nums):
    if idx == M:
        print(*nums)
        return

    start = nums[len(nums) - 1] if nums else 1
    for i in range(start, N + 1):
        nums.append(i)
        recursion(idx + 1, nums)
        nums.pop()


N, M = map(int, input().split())

recursion(0, [])
