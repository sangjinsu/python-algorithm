import sys
from functools import reduce

number = int(sys.stdin.readline().strip())
cycle = 0
new_number = number
while True:
    total = reduce(lambda x, y: int(x) + int(y), str(new_number))
    new_number = int(str(new_number)[-1] + str(total)[-1])
    cycle += 1
    if number == new_number:
        break


sys.stdout.write(str(cycle))
