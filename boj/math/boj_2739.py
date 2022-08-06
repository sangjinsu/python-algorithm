import sys

N = int(sys.stdin.readline().strip())
[sys.stdout.write("{} * {} = {}\n".format(N, i, N * i)) for i in range(1, 10)]
