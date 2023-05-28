import sys

if __name__ == '__main__':
    N, L = map(int, sys.stdin.readline().strip().split())
    pipe = [False for _ in range(1001)]
    for hole in map(int, sys.stdin.readline().strip().split()):
        pipe[hole] = True

    result = 0
    for i, hole in enumerate(pipe):
        if hole:
            result += 1
            for j in range(i, i + L):
                if j > 1000:
                    break
                pipe[j] = False

    sys.stdout.write(str(result))