import sys

N = int(sys.stdin.readline())
nums = map(int, list(sys.stdin.readline().strip()))
sys.stdout.write(str(sum(nums)))
