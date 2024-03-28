import sys
import time
sys.stdin = open('input1764.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
no_d = [input().strip() for _ in range(N)]
no_b = [input().strip() for _ in range(N)]
ans = []
no_d = set(no_d)
no_b = set(no_b)
for i in no_b:
    if i in no_d:
        ans.append(i)

ans.sort()
print(len(ans))
for i in ans:
    print(i)