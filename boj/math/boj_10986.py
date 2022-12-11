import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = map(int, sys.stdin.readline().strip().split())

snum = []
temp = 0
for num in nums:
    temp += num
    snum.append(temp)

sremainders = [0] * M
remainders = [num % M for num in snum]
for remainder in remainders:
    sremainders[remainder] += 1

result = sremainders[0]
for remainder in sremainders:
    if remainder > 1:
        result += remainder * (remainder - 1) // 2

sys.stdout.write(str(result))
