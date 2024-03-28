import sys
sys.stdin = open('input1912.txt')
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
di = [0] * n
di[0] = arr[0]
for i in range(1, n):
    di[i] = max(di[i-1] + arr[i], arr[i])

print(max(di))