import sys

switch_num = int(sys.stdin.readline().strip())
switches = [0] + list(map(int, sys.stdin.readline().strip().split()))
student_num = int(sys.stdin.readline().strip())
students = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(student_num)]

for s in students:
    if s[0] == 1:
        for i in range(s[1], switch_num + 1, s[1]):
            switches[i] = 0 if switches[i] else 1
    elif s[0] == 2:
        switches[s[1]] = 0 if switches[s[1]] else 1
        i = 1
        while s[1] - i >= 1 and s[1] + i < switch_num + 1 and switches[s[1] - i] == switches[s[1] + i]:
            switches[s[1] - i] = 0 if switches[s[1] - i] else 1
            switches[s[1] + i] = 0 if switches[s[1] + i] else 1
            i += 1

for i in range(1, switch_num + 1):
    sys.stdout.write(str(switches[i]) + ' ')
    if i % 20 == 0:
        sys.stdout.write('\n')
