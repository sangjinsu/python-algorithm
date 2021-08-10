test_cases = int(input())

for t in range(1, test_cases + 1):
    N = int(input())
    nums = map(int, input().strip().split())
    min_num, max_num = 1000001, 0
    for num in nums:
        if max_num < num:
            max_num = num

        if min_num > num:
            min_num = num

    result = max_num - min_num
    print(f'#{t} {result}')
