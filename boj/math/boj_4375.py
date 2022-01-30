while True:
    try:
        n = int(input().strip())
    except EOFError:
        break

    x = 1
    while True:
        if x % n == 0:
            print(len(str(x)))
            break
        x = 10 * x + 1
