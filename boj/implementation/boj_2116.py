import sys

n = int(sys.stdin.readline().strip())
dices = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# A B C D E F
side = [5, 3, 4, 1, 2, 0]

max_tot = 0
for bottom in range(1, 7):
    tot = 0
    for dice in dices:
        b = dice.index(bottom)
        t = side[b]
        bottom = dice[t]

        d = dice[:]
        d.remove(dice[b])
        d.remove(dice[t])
        tot += max(d)
    max_tot = max(max_tot, tot)

sys.stdout.write(str(max_tot))
