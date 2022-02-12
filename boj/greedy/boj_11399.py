N = int(input())
nums = list(map(int, input().strip().split()))

nums.sort()
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]

print(sum(nums))
