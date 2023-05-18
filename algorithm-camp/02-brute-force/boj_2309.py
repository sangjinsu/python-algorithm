import sys
from itertools import combinations

if __name__ == '__main__':
    heights = [int(sys.stdin.readline()) for _ in range(9)]
    combs = list(combinations(heights, 7))
    for comb in combs:
        if sum(comb) == 100:
            comb_list = sorted(comb)
            for v in comb_list:
                sys.stdout.write(str(v) + '\n')
            break
