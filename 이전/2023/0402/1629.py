import sys
sys.stdin = open('input1629.txt')
input = sys.stdin.readline

# def power(n, m):
#     if m == 0:
#         return 1
#     elif m % 2 == 0:
#         return power(n*n, m//2)
#     else:
#         return n * power(n*n, (m-1)//2)

# def power(n, m):
#     result = 1
#     while m > 0:
#         if m % 2 == 1:
#             result *= n
#         n *= n
#         m //= 2
#     return result

def mod_power(n, m, k):
    result = 1
    n = n % k
    while m > 0:
        if m % 2 == 1:
            result = (result * n) % k
        n = (n * n) % k
        m //= 2
    return result


A, B, C = map(int, input().split())
# A의 B제곱 -> A의 2제곱 실행, A의 2제곱끼리 곱셈,
# A의 제곱 실행, A에 대입
# A의 제곱 실행, A에 대입
# A의 제곱 실행, A에 대입
# 3번 실행, 결과는 A의8승 계산
# ans = power(A, B) % C
print(mod_power(A, B, C))