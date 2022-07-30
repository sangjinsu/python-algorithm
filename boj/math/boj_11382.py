import sys

a, b, c = map(int, sys.stdin.readline().strip().split())
result = a + b + c
sys.stdout.write(str(result))
