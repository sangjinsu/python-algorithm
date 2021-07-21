import sys

n = int(sys.stdin.readline().strip())

sticks = list()

for i in range(n):
    stick = int(sys.stdin.readline().strip())
    sticks.append(stick)

highest = 0
count = 0
for i in range(n):
    stick = sticks.pop()
    if highest < stick:
        count += 1
        highest = stick

sys.stdout.write(str(count) + '\n')
