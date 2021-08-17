test_cases = int(input().strip())

grade = ('A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0')

for t in range(1, test_cases + 1):
    n, k = tuple(map(int, input().strip().split()))
    scores = [(i, *map(int, input().strip().split())) for i in range(1, n + 1)]
    scores.sort(key=lambda score: score[1] * .35 + score[2] * .45 + score[3] * .2, reverse=True)
    for i in range(len(scores)):
        if scores[i][0] == k:
            print(f'#{t} {grade[i // (n // 10)]}')
