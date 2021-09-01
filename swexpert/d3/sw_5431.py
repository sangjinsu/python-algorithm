test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n, k = map(int, input().strip().split())
    passed = input().strip().split()
    students = [str(i) for i in range(1, n + 1)]

    for p in passed:
        students.remove(p)

    print('#{} {}'.format(t, ' '.join(students)))
