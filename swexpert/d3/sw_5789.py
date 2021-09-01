test_cases = int(input())

for t in range(1, test_cases + 1):
    n, q = map(int, input().split())
    nums = [0] * n
    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            nums[j-1] = i

    print('#{} {}'.format(t, ' '.join(map(str, nums))))


