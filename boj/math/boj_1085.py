import sys

x, y, w, h = map(int, sys.stdin.readline().strip().split())

result = min([x, y, w - x, h - y])
sys.stdout.write(str(result))
