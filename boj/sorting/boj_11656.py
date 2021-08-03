import sys

word = sys.stdin.readline().strip()

suffixes = [word[i:] for i in range(len(word))]

for suffix in sorted(suffixes):
    sys.stdout.write(suffix + '\n')
