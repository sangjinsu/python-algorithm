import sys

word = sys.stdin.readline().strip()
result = [0] * (ord('z') - ord('a') + 1)
for letter in word:
    result[ord(letter) - ord('a')] += 1

sys.stdout.write(' '.join(map(str, result)))
