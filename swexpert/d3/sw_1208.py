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
