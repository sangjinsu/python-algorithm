def recursion(idx, nums):
    if idx == M:
        print(*nums)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            nums.append(input_nums[i])
            recursion(idx + 1, nums)
            nums.pop()
            visited[i] = False


N, M = map(int, input().split())
input_nums = sorted(list(map(int, input().split())))
visited = [False] * N
recursion(0, [])
