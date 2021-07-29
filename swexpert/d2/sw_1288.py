test_cases = int(input())

for i in range(1, test_cases + 1):
    nums = [str(i) for i in range(10)]
    num = int(input())

    N = 0
    while nums:
        N += 1
        sheep = N * num
        digits = list(str(sheep))

        for digit in digits:
            if digit in nums:
                nums.remove(digit)

    result = N * num
    print('#{} {}'.format(i, result))

