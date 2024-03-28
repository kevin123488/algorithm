import sys
sys.stdin = open('input11444.txt')
input = sys.stdin.readline

def matrix_mul(a, b):
    n = len(a)
    m = len(b[0])
    new_matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(b)):
                new_matrix[i][j] += a[i][k] * b[k][j]
    return new_matrix

def matrix_pow(matrix, p):
    if p == 1:
        return matrix
    elif p % 2 == 0:
        temp = matrix_pow(matrix, p//2)
        return matrix_mul(temp, temp)
    else:
        temp = matrix_pow(matrix, (p-1)//2)
        return matrix_mul(matrix_mul(temp, temp), matrix)

def fibonacci(n):
    if n <= 1:
        return n
    matrix = [[1, 1], [1, 0]]
    matrix = matrix_pow(matrix, n-1)
    return matrix[0][0]


n = int(input())
# pi = [0] * (n + 1)
# pi[1] = 1
# for i in range(2, n + 1):
#     pi[i] = pi[i-1] + pi[i-2]
#
# print(pi[n]%1000000007)

# 위 방식은 일반적인 dp
# 분할정복으로 조금 더 빠르게 수행해보자
print(fibonacci(n))