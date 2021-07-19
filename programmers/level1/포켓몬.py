def solution(nums):
    nums_set = set(nums)
    n = len(nums_set)
    m = len(nums) // 2

    result = m if n >= m else n
    return result
