import sys

n, k = map(int, sys.stdin.readline().strip().split())

temp = list(map(int, sys.stdin.readline().strip().split()))

"""
10 5
3 -2 -4 -9 0 3 7 13 8 -3
"""
start = 0
end = k
tot = sum(temp[:k])
max_temp = tot
for i in range(n - k):
    tot = tot - temp[start + i] + temp[end + i]
    max_temp = max(max_temp, tot)

sys.stdout.write(str(max_temp))
