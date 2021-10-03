import sys


def recursion(idx, word):
    if len(word) == L:
        aeiou = 0
        for letter in word:
            if letter in 'aeiou':
                aeiou += 1
        if aeiou >= 1 and L - aeiou >= 2:
            sys.stdout.write(word + '\n')
        return

    if idx >= C:
        return

    recursion(idx + 1, word + letters[idx])
    recursion(idx + 1, word)


L, C = map(int, sys.stdin.readline().strip().split())
letters = sys.stdin.readline().strip().split()
letters.sort()
recursion(0, '')

