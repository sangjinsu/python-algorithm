import sys

thirtyNums = [True] * 31

for _ in range(28):
    thirtyNums[int(sys.stdin.readline())] = False

for i in range(1, 31):
    if thirtyNums[i]:
        sys.stdout.write(str(i) + '\n')
