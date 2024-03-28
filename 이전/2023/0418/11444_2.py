import sys
sys.stdin = open('input11444.txt')
input = sys.stdin.readline

def multiply_matrix(matrix1, matrix2, mod):
    n = len(matrix1)
    m = len(matrix2[0])
    new_matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(matrix2)):
                new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
                new_matrix[i][j] %= mod
    return new_matrix

def power_matrix(matrix, power, mod):
    if power == 1:
        return matrix
    elif power % 2 == 0:
        half = power_matrix(matrix, power // 2, mod)
        return multiply_matrix(half, half, mod)
    else:
        half = power_matrix(matrix, (power - 1) // 2, mod)
        temp = multiply_matrix(half, half, mod)
        return multiply_matrix(matrix, temp, mod)

def fibonacci(n, mod):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    matrix = [[1, 1], [1, 0]]
    result = power_matrix(matrix, n - 1, mod)
    return result[0][0]

n = int(input())
mod = 1000000
print(fibonacci(n, mod))