N = int(input())
nums = list(map(int, input().split()))
find = False

for i in range(N - 1, 0, -1):
    if nums[i - 1] < nums[i]:
        for j in range(N - 1, 0, -1):
            if nums[i - 1] < nums[j]:
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                nums = nums[:i] + sorted(nums[i:])
                find = True
                break
        if find:
            print(*nums)
            break
if not find:
    print(-1)
