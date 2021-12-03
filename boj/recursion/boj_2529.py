def recursion(idx, value):
    if idx == K:
        results.append(value)
        return

    before_index = -1 if len(value) >= 2 else 0

    if signs[idx] == '<':
        for num in nums:
            if not visited[num]:
                if int(value[before_index]) < num:
                    visited[num] = True
                    recursion(idx + 1, value + str(num))
                    visited[num] = False
    else:
        for num in nums:
            if not visited[num]:
                if int(value[before_index]) > num:
                    visited[num] = True
                    recursion(idx + 1, value + str(num))
                    visited[num] = False


K = int(input())
signs = input().split()
nums = [i for i in range(10)]
visited = [False] * 10
results = []
for num in nums:
    visited[num] = True
    recursion(0, str(num))
    visited[num] = False

print(max(results))
print(min(results))
