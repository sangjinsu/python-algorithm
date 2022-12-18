import sys

n = int(sys.stdin.readline().strip())
cnt, total = 0, 0
start, end = 0, 0

while end <= n:
    if total < n:
        end += 1
        total += end
    elif total > n:
        total -= start
        start += 1
    else:
        cnt += 1
        end += 1
        total += end

sys.stdout.write(str(cnt))
