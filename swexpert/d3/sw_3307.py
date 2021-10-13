test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N = int(input().strip())
    nums = list(map(int, input().strip().split()))
    # 6 2 3 1 5 6
    dp = [1] * N
    # 1 1 2 1 3 1
    # 2 3 5 6
    for i in range(1, N):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    print('#{} {}'.format(t, max(dp)))
