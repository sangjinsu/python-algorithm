import sys

nums = list(map(int, sys.stdin.readline().strip().split(' ')))

num1 = max(nums)
num2 = min(nums)

while True:
    temp = num1 % num2
    if temp == 0:
        break
    num1, num2 = num2, temp

gcd = num2
lcm = num2 * (nums[0] // num2) * (nums[1] // num2)

sys.stdout.write(str(gcd) + '\n')
sys.stdout.write(str(lcm))
