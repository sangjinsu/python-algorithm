import sys


def rot13(letter, first, end):
    next_letter = ord(letter) + 13
    if next_letter > ord(end):
        next_letter = next_letter - ord(end) + ord(first) - 1
    return chr(next_letter)


sentence = sys.stdin.readline().rstrip('\n')

result = ''

for letter in sentence:
    if letter.islower():
        result += rot13(letter, 'a', 'z')
    elif letter.isupper():
        result += rot13(letter, 'A', 'Z')
    else:
        result += letter

sys.stdout.write(result)
