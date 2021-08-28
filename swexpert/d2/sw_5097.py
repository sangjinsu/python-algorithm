# 회전
test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n, m = map(int, input().strip().split())
    queue = list(map(int, input().strip().split()))
    front = 0
    i = 0
    while i < m:
        i += 1
        front = (front + 1) % n

    print('#{} {}'.format(t, queue[front]))
