import sys

_, X = map(int, sys.stdin.readline().strip().split())
nums = map(int, sys.stdin.readline().strip().split())
result = ' '.join([str(num) for num in nums if num < X])
sys.stdout.write(str(result))
