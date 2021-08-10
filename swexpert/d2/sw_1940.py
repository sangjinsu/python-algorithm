test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n = int(input().strip())
    meter = 0
    speed = 0
    for i in range(n):
        commands = list(map(int, input().strip().split()))
        if commands[0] == 1:
            speed += commands[1]
        elif commands[0] == 2:
            speed -= commands[1]
            if speed < 0:
                speed = 0
        meter += speed

    print('#{} {}'.format(t, meter))

