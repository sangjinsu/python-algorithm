import sys

maxNum = 0
maxIndex = -1

for i in range(9):
    num = int(sys.stdin.readline())
    if num > maxNum:
        maxNum = num
        maxIndex = i + 1

sys.stdout.write(str(maxNum) + '\n')
sys.stdout.write(str(maxIndex))
