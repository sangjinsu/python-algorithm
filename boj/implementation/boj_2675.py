import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    R, S = sys.stdin.readline().strip().split()
    sys.stdout.write(''.join([ch * int(R) for ch in S]) + '\n')
