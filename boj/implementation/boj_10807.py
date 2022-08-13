import sys

_ = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
v = int(sys.stdin.readline().strip())

sys.stdout.write(str(nums.count(v)))
