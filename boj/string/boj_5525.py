import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

P = 'IO' * N + 'I'
htable = {P: 0}
for i in range(0, M + 1 - len(P)):
    s_part = S[i: i + len(P)]
    if s_part == P:
        htable[s_part] += 1

sys.stdout.write(str(htable[P]))
