import sys
from collections import deque

s = sys.stdin.readline().strip()

deq = deque()

result = ''
isIn = False
for letter in s:
    if letter == '<' or (letter == ' ' and not isIn):
        while deq:
            result += deq.pop()
        result += letter
        if letter == '<':
            isIn = True

    elif letter == '>':
        while deq:
            result += deq.popleft()
        result += letter
        isIn = False

    else:
        deq.append(letter)

while deq:
    result += deq.pop()
sys.stdout.write(result)
