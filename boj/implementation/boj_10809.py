import sys

word = sys.stdin.readline().strip()

result = [-1] * (ord('z') - ord('a') + 1)

for i, letter in enumerate(word):
    if result[ord(letter) - ord('a')] == -1:
        result[ord(letter) - ord('a')] = i

sys.stdout.write(' '.join(map(str, result)))
