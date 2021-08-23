def subset(nums):
    for i in range(1, 2 ** len(nums)):
        sub = []
        for j in range(len(nums) + 1):
            if i & (1 << j):
                sub.append(nums[j])
        print(sub)


subset([3, 6, 7, 1, 5, 4])
