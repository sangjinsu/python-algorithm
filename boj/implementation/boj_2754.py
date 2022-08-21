import sys


def solve():
    grade = list(sys.stdin.readline().strip())
    main_grade = dict(A=4, B=3, C=2, D=1, F=0)
    result = main_grade.get(grade[0])
    if len(grade) == 2:
        if grade[1] == '+':
            result += 0.3
        if grade[1] == '-':
            result -= 0.3

    return result


sys.stdout.write('{0:0.1f}'.format(solve()))
