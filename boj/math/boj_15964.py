import sys

A, B = map(int, sys.stdin.readline().split())
result = pow(A, 2) - pow(B, 2)
sys.stdout.write(str(result))
