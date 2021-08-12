# 특별한 정렬

test_cases = int(input().strip())


def special_sort(lst):
    nums = lst[:]
    for i in range(len(nums) - 1):
        idx = i
        for j in range(i + 1, len(nums)):
            if i % 2:
                if nums[idx] > nums[j]:
                    idx = j
            else:
                if nums[idx] < nums[j]:
                    idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
    return nums


for t in range(1, test_cases + 1):
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))

    sorted_nums = special_sort(nums)

    print('#{} {}'.format(t, ' '.join(map(str, sorted_nums[:10]))))
