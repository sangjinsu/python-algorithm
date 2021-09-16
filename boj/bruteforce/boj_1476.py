import sys

years = list(map(int, sys.stdin.readline().strip().split()))

year = 1
that_year = [1, 1, 1]

while True:
    if that_year[0] == years[0] and that_year[1] == years[1] and that_year[2] == years[2]:
        break
    year += 1
    that_year[0] = (that_year[0] + 1) % 16
    if that_year[0] == 0:
        that_year[0] += 1

    that_year[1] = (that_year[1] + 1) % 29
    if that_year[1] == 0:
        that_year[1] += 1

    that_year[2] = (that_year[2] + 1) % 20
    if that_year[2] == 0:
        that_year[2] += 1

sys.stdout.write(str(year))
