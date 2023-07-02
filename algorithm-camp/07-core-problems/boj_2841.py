import sys

if __name__ == '__main__':
    N, P = map(int, sys.stdin.readline().split())
    flats = [[] for _ in range(N + 1)]
    result = 0
    for _ in range(N):
        line, flat = map(int, sys.stdin.readline().split())
        while flats[line] and flats[line][-1] > flat:
            flats[line].pop()
            result += 1
        if flats[line] and flats[line][-1] == flat:
            continue

        flats[line].append(flat)
        result += 1

    sys.stdout.write(str(result))
