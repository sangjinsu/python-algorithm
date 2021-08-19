test_cases = int(input().strip())

# 동적 계획법
for t in range(1, test_cases + 1):
    n = int(input().strip()) // 10
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2

    print('#{} {}'.format(t, dp[-1]))


# 재귀
# def stick_paper(n):
#     if n <= 1:
#         return 1
#     return stick_paper(n - 1) + stick_paper(n - 2) * 2
#
#
# for t in range(1, test_cases + 1):
#     n = int(input().strip()) // 10
#     result = stick_paper(n)
#
#     print('#{} {}'.format(t, result))
