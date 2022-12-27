import sys

N = int(sys.stdin.readline().strip())

nums = list()
for i in range(N):
    nums.append((int(sys.stdin.readline().strip()), i))

sorted_nums = sorted(nums)

result = 0
for i in range(N):
    result = max(result, sorted_nums[i][1] - i)

result += 1
sys.stdout.write(str(result))
