def is_Prime():
    check = [True] * 3001
    check[0], check[1] = False, False
    m = int(3001 ** 0.5)
    for i in range(2, m + 1):
        if check[i]:
            for j in range(i + i, 3001, i):
                check[j] = False
    return check


def solution(nums):
    result = 0
    primes = is_Prime()
    length = len(nums)
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if primes[nums[i] + nums[j] + nums[k]]:
                    result += 1
    return result
