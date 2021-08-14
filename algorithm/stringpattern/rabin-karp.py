# rabin - karp algorithm
# 해쉬 값을 사용
# 'abc'
# 'a' => 97
# 'b' => 98
# 'c' => 99
# hash value = 97 * 2^0 + 98 + 2^1 + 99 *  2^2
# 시간 복잡도: O(n)
# 만약 충돌이 발생한다면 문자 값들이 모두 맞는지 확인하는 작업이 필요하다

def hash_str(s):
    k = 2 * (len(s) - 1)
    v = 0
    for c in s:
        v += ord(c) * k
        k //= 2
    return v


def ravin_karp(pattern, string):
    hash_p = hash_str(pattern)

    hash_v = hash_str(string[:len(pattern)])
    for i in range(1, len(string) - len(pattern) + 1):
        print(hash_p, hash_v)
        if hash_p == hash_v:
            print(i)
            break
        hash_v = 2 * (hash_v - ord(string[i - 1]) * (len(pattern) - 1) * 2) + ord(string[i + len(pattern)])


ravin_karp('dc', 'abdddddc')
