
T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    N = 0
    while len(nums) > 0:
        N += 1
        sheep = N * num
        digits = list(str(sheep))
        print(digits)
        for digit in digits:
            if digit in nums:
                nums.remove(digit)
    result = N * num
    print('#{} {}'.format(test_case, result))
