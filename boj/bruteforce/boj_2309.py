import sys

nums = [int(sys.stdin.readline()) for _ in range(9)]
tot = sum(nums)

for i in range(9):
    for j in range(i + 1, 9):
        if 100 == tot - (nums[i] + nums[j]):
            num1, num2 = nums[i], nums[j]
            nums.remove(num1)
            nums.remove(num2)
            break

    if len(nums) == 7:
        break

nums.sort()

for i in range(7):
    sys.stdout.write(str(nums[i]) + '\n')
