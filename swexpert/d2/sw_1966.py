test_cases = int(input().strip())


def bubble_sort(lst):
    nums = lst[:]

    swap = True
    for i in range(len(nums) - 1, -1, -1):
        if not swap:
            break
        swap = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap = True

    return nums


for t in range(1, test_cases + 1):
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))

    sorted_nums = bubble_sort(nums)
    result = ''

    for num in sorted_nums:
        result += str(num) + ' '

    print('#{} {}'.format(t, result))
