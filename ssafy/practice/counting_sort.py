def counting_sort(nums):
    m = 0
    for num in nums:
        if m < num:
            m = num

    counts = [0] * (m + 1)
    for num in nums:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i - 1]

    sorted_nums = [-1] * len(nums)
    for num in nums:
        sorted_nums[counts[num] - 1] = num
        counts[num] -= 1

    print(sorted_nums)


nums = [1, 2, 5, 8, 9, 6, 4, 7, 5]
counting_sort(nums)
