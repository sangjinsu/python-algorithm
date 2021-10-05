import sys

N = int(sys.stdin.readline().strip())
lines = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

lines.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = lines[0][1]
print(lines)
for i in range(1, N):
    if lines[i][0] >= end:
        cnt += 1
        end = lines[i][1]

sys.stdout.write(str(cnt))
