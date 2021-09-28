test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N, *commands = input().strip().split()

    orange_pos = 1
    blue_pos = 1

    orange_queue = []
    blue_queue = []

    N = int(N)
    cmds = []
    for i in range(0, N * 2, 2):
        command = commands[i]
        pos = int(commands[i + 1])
        if command == 'O':
            orange_queue.append(pos)
        else:
            blue_queue.append(pos)
        cmds.append(command)

    time = 0
    while orange_queue or blue_queue:
        time += 1
        check = False
        if orange_queue:
            if orange_queue[0] == orange_pos and cmds[0] == 'O':
                orange_queue.pop(0)
                check = True
            elif orange_queue[0] < orange_pos:
                orange_pos -= 1
            elif orange_queue[0] > orange_pos:
                orange_pos += 1

        if blue_queue:
            if blue_queue[0] == blue_pos and cmds[0] == 'B':
                blue_queue.pop(0)
                check = True
            elif blue_queue[0] < blue_pos:
                blue_pos -= 1
            elif blue_queue[0] > blue_pos:
                blue_pos += 1
        if check:
            cmds.pop(0)

    print('#{} {}'.format(t, time))
