test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N = int(input().strip())

    sentence = input().strip()
    check = ('!', '?', '.')
    idx = 0
    result = []
    # my name is Hye Soo. my id is Rhs0266. what your id Bro?
    for i in range(len(sentence)):
        # 문장 쪼개기
        if not sentence[i] in check:
            continue
        temp = sentence[idx:i]
        idx = i + 2
        """
        my name is Hye Soo
        my id is Rhs0266
        what your id Bro
        """

        # 체크
        cnt = 0
        words = temp.split()
        for word in words:
            if not word[0].isupper():
                continue
            if not word.isalpha():
                continue
            if len(word) == 1 or word[1:].islower():
                cnt += 1
        result.append(cnt)
    print('#{}'.format(t), end=' ')
    print(*result)
