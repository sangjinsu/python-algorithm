T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # p : A사 1리터당 요금
    # q : B사 R리터 이하 기본요금
    # r : B사 기준 리터
    # s : B사  1리터당 추가 요금
    # w : 수도 사용량
    p, q, r, s, w = tuple(map(int, input().split()))

    companyA = p * w
    companyB = q + (w - r) * s if w > r else q 

    result = companyA if companyA < companyB else companyB
    print('#{} {}'.format(test_case, result))
