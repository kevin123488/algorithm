import sys
sys.stdin = open('input11053.txt')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
di = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            di[i] = max(di[i], di[j] + 1)

print(max(di))