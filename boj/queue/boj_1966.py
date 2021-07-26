import sys

testCases = int(sys.stdin.readline().strip())

for i in range(testCases):
    n, index = tuple(map(int, sys.stdin.readline().strip().split()))

    queue = list(map(int, sys.stdin.readline().strip().split()))

    cnt = 0
    while True:
        max_num = max(queue)

        item = queue[0]
        queue = queue[1:]
        if item == max_num and index == 0:
            cnt += 1
            break
        elif item == max_num:
            cnt += 1
        else:
            queue.append(item)

        index -= 1
        if index < 0:
            index += len(queue)

    sys.stdout.write(str(cnt) + '\n')
