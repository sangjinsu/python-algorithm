import sys

n, m = map(int, sys.stdin.readline().strip().split())
k = int(sys.stdin.readline().strip())
dotted = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(k)]

row_cuts = [0]
col_cuts = [0]

for dot in dotted:
    if dot[0] == 0:
        row_cuts.append(dot[1])
    if dot[0] == 1:
        col_cuts.append(dot[1])

row_cuts.append(m)
col_cuts.append(n)

row_cuts.sort()
col_cuts.sort()

cut_row = []
cut_col = []

for i in range(1, len(row_cuts)):
    cut_row.append(row_cuts[i] - row_cuts[i - 1])

for i in range(1, len(col_cuts)):
    cut_col.append(col_cuts[i] - col_cuts[i - 1])

cut_row.sort()
cut_col.sort()

result = cut_col[-1] * cut_row[-1]

sys.stdout.write(str(result))
