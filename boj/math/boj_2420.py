import sys

N, M = map(int, sys.stdin.readline().strip().split())
result = abs(N - M)
sys.stdout.write(str(result))
