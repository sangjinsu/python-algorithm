test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N = int(input().strip())

    nums = ''
    while len(nums) < N:
        nums += ''.join(input().split())

    num = 0
    while True:
        if str(num) not in nums:
            break
        num += 1

    print('#{} {}'.format(t, num))
