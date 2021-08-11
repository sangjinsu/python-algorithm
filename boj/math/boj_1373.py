import sys

binary = sys.stdin.readline().strip()

for i in range(len(binary), 0, -3):
    if i < 3:
        print(binary[:i])
    else:
        print(binary[i - 3: i])
