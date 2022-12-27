import sys
from functools import reduce

nums = list(sys.stdin.readline().strip())
nums.sort(reverse=True)
result = reduce(lambda acc, num: acc + num, nums, '')
sys.stdout.write(result)
