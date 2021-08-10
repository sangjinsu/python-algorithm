test_cases = 10


def bubble_sort(lst):
    nums = lst[:]
    check = True
    for i in range(len(nums) - 1, 0, -1):
        if not check:
            break
        check = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                check = True
    return nums


def counting_sort(lst):
    nums = lst[:]

    max_num = 0
    for num in nums:
        if max_num < num:
            max_num = num

    counts = [0] * (max_num + 1)
    for num in nums:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] = counts[i - 1] + counts[i]

    new_lst = [-1] * len(nums)
    for num in nums:
        new_lst[counts[num] - 1] = num
        counts[num] -= 1

    return new_lst


for t in range(1, test_cases + 1):
    n = int(input().strip())
    boxes = list(map(int, input().strip().split()))

    sorted_boxes = bubble_sort(boxes)
    for i in range(n):
        sorted_boxes[-1] -= 1
        sorted_boxes[0] += 1
        if sorted_boxes[-1] < sorted_boxes[-2] or sorted_boxes[0] > sorted_boxes[1]:
            sorted_boxes = bubble_sort(sorted_boxes)

    result = sorted_boxes[-1] - sorted_boxes[0]
    print('#{} {}'.format(t, result))
