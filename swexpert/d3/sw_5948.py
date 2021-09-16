test_cases = int(input())

for t in range(1, test_cases + 1):
    nums = list(map(int, input().strip().split()))
    result = []
    for i in range(0, 5):
        for j in range(i + 1, 6):
            for k in range(j + 1, 7):
                result.append(nums[i] + nums[j] + nums[k])
    result = sorted(list(set(result)), reverse=True)
    print('#{} {}'.format(t, result[4]))
