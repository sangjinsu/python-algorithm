import sys

n = int(sys.stdin.readline().strip())
rows = [0] * n
cnt = 0

def n_qeens(k):
    global cnt
    if k == n:
        cnt += 1
        return

    for x in range(n):
        ko = 1
        for y in range(k):
            if rows[y] == x or k - y == abs(x - rows[y]):
                ko = 0
                break
        if ko:
            rows[k] = x
            n_qeens(k + 1)

n_qeens(0)
sys.stdout.write(str(cnt))
