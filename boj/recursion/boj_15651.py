def recursion(nums):
    if len(nums) == M:
        print(*nums)
        return

    for i in range(1, N + 1):
        nums.append(i)
        recursion(nums)
        nums.pop()


N, M = map(int, input().split())
visited = [False] * (N + 1)
recursion([])
