test_cases = int(input().strip())

# i     0 1 2 3 4 5
# p     1 1 0 0 1 1
# need  0 0 0 0 2 2
# tot   1 2 2 2 4 5

for t in range(1, test_cases + 1):
    people = input().strip()
    tot = 0
    need = 0
    for i in range(len(people)):
        if i > tot and people[i] != '0':
            need += i - tot
            tot = i
        tot += int(people[i])
    print('#{} {}'.format(t, need))
