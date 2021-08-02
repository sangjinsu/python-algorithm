import sys

nums = sys.stdin.readline().strip().split(' ')

num1 = int(nums[0] + nums[1])
num2 = int(nums[2] + nums[3])

sys.stdout.write(str(num1 + num2))
