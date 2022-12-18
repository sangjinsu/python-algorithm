N = int(input())
nums = list(map(int, input().strip().split()))
nums.sort()

cnt = 0
for i in range(N):
    temp = nums[:i] + nums[i + 1:]
    left = 0
    right = N - 2
    while left < right:
        total = temp[left] + temp[right]
        if total == nums[i]:
            cnt += 1
            break
        elif total > nums[i]:
            right -= 1
        else:
            left += 1

print(cnt)
