test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    vote = [0] * N
    for b in range(M):
        for a in range(N):
            if B[b] >= A[a]:
                vote[a] += 1
                break
    result = vote.index(max(vote)) + 1
    print('#{} {}'.format(t, result))
