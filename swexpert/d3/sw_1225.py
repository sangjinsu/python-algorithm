test_cases = 10

for t in range(1, test_cases + 1):
    test_num = int(input())
    queue = list(map(int, input().strip().split()))
    front = 0
    rear = len(queue) - 1
    i = 0
    while queue[rear] > 0:
        queue[front] -= i + 1
        i = (i + 1) % 5
        front = (front + 1) % 8
        rear = (rear + 1) % 8
    queue[rear] = 0

    print('#%d ' % t, end='')
    while front != rear:
        print('%d' % queue[front], end=' ')
        front = (front + 1) % 8
    print('%d' % queue[front])
