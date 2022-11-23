import math
import sys

A, B, V = map(int, sys.stdin.readline().strip().split())

day = math.ceil(V / (A-B))

print(day)