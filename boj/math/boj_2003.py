import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

start = 0
end = 1

cnt = 0
while True:
    total = sum(nums[start:end])
    if total < M:
        end += 1
    if total >= M:
        start += 1

    if end > N:
        break

    if total == M:
        cnt += 1

sys.stdout.write(str(cnt))
