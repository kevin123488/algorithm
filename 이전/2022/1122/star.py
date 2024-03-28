import sys
sys.stdin = open("starinput.txt")

T = int(input())
for i in range(T):
    k = int(input())
    ans = '*'*k
    print(f'{i+1}')