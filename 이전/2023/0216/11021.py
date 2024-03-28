import sys
sys.stdin = open('11021input.txt')

T = int(input())
for i in range(T):
    A ,B = map(int, input().split())
    print(f'Case #{i+1}: {A+B}')