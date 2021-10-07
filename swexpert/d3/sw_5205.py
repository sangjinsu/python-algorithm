# 퀵정렬
# Lomuto partition 1개 시간초과..
# 중간 위치 값을 활용한 퀵 정렬 1개 시간초과..
def quickSort(arr, left, right):
    if left < right:
        s = partitionM(arr, left, right)
        quickSort(arr, left, s - 1)
        quickSort(arr, s + 1, right)


# Hoare-Partition
def partitionHP(arr, left, right):
    pivot = left
    i, j = left + 1, right
    while i <= j:
        while i <= right and arr[i] <= arr[pivot]:
            i += 1
        while j > left and arr[j] >= arr[pivot]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j


# Lomuto partition
def partitionL(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


# 중간값을 활용한 퀵 정렬
def partitionM(arr, left, right):
    mid = (left + right) // 2
    arr[left], arr[mid] = arr[mid], arr[left]
    pivot = left
    i, j = left + 1, right

    while i <= j:
        while i <= right and arr[i] <= arr[pivot]:
            i += 1
        while j > left and arr[j] >= arr[pivot]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    nums = list(map(int, input().strip().split()))
    quickSort(nums, 0, len(nums) - 1)
    print('#{} {}'.format(t, nums[N // 2]))
