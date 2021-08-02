import sys

while True:
    sentence = sys.stdin.readline().rstrip('\n')
    if not sentence:
        break

    big, small, number, blank = 0, 0, 0, 0
    for letter in sentence:
        if 'a' <= letter <= 'z':
            small += 1
        elif 'A' <= letter <= 'Z':
            big += 1
        elif '0' <= letter <= '9':
            number += 1
        else:
            blank += 1

    sys.stdout.write(f'{small} {big} {number} {blank}\n')
