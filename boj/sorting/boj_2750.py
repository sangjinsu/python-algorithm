N = int(input())

nums = list()
for i in range(N):
    nums.append(int(input()))

nums.sort()
for num in nums:
    print(num)