def gcd(A, B):
    while A != 0:
        B, A = A, B % A
    return B


A, B = map(int, input().split())

if A >= B:
    GCD = gcd(B, A)
else:
    GCD = gcd(A, B)

result = A * B // GCD
print(result)
