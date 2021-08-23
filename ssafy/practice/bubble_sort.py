def bubble_sort(nums):
    change = True
    for i in range(len(nums) - 1, -1, -1):
        if not change:
            break
        change = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                change = True
    return nums


nums = [9, 8, 6, 7, 5, 2, 4, 7, 8, 9, 3, 2]
print(bubble_sort(nums))
