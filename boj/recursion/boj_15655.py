def recursion(depth, value):
    if depth == M:
        print(*value)
        return
    for i in range(N):
        if not visited[i] and value[-1] <= nums[i]:
            visited[i] = True
            value.append(nums[i])
            recursion(depth + 1, value)
            value.pop()
            visited[i] = False


N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
nums.sort()

visited = [False] * N
for i in range(N):
    visited[i] = True
    recursion(1, [nums[i]])
    visited[i] = False
