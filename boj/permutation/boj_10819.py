def recursion(idx, values):
    global result
    if idx == N:
        total = 0
        for i in range(0, N-1):
            total += abs(values[i] - values[i + 1])
        result = max(result, total)
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            values.append(nums[i])
            recursion(idx + 1, values)
            visited[i] = False
            values.pop()


N = int(input().strip())

nums = list(map(int, input().strip().split()))
visited = [False] * N
result = 0
recursion(0, [])
print(result)