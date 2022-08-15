import sys

chars = sys.stdin.readline()
result = ''
for c in chars:
    if c.islower():
        result += c.upper()
    else:
        result += c.lower()
sys.stdout.write(result)
