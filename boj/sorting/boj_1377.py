N = int(input())

nums = list()
for i in range(N):
    nums.append((int(input()), i))

sorted_nums = sorted(nums)

result = 0
for i in range(N):
    result = max(result, sorted_nums[i][1] - nums[i][1])

result += 1
print(result)
