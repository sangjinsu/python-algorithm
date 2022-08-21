import sys

word = sys.stdin.readline().strip()

result = [-1] * (ord('z') - ord('a') + 1)
idx_chars = [(i, word[i]) for i in range(len(word))]

for idx_char in idx_chars:
    idx = ord(idx_char[1]) - ord('a')
    if result[idx] < 0:
        result[idx] = idx_char[0]

sys.stdout.write(' '.join(map(str, result)))
