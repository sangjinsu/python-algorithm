test_cases = int(input().strip())


def sum_sub_nums(idx, value):
    global result
    if value == K:
        result += 1
        return
    if value > K or idx >= N:
        return

    sum_sub_nums(idx + 1, value)
    sum_sub_nums(idx + 1, value + nums[idx])


for t in range(1, test_cases + 1):
    N, K = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    result = 0
    sum_sub_nums(0, 0)
    print('#{} {}'.format(t, result))
