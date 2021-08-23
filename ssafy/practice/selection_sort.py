def selection_sort(nums):
    for i in range(len(nums) - 1):
        idx = i
        for j in range(i + 1, len(nums)):
            if nums[idx] > nums[j]:
                idx = j
        nums[idx], nums[i] = nums[i], nums[idx]
    print(nums)


selection_sort([3, 5, 6, 9, 4, 4, 1, 2])
