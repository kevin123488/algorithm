import sys
sys.stdin = open('input11403.txt')
from collections import deque
input = sys.stdin.readline

def find_ans(start, end):
    q = deque()
    for i in range(n):
        if arr[start][i] == 1:
            q.append(i)
    while q:
        now = q.popleft()
        if now == end:
            return 1

        for i in range(n):
            if arr[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)

    return 0

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[0] * n for __ in range(n)]
for i in range(n):
    for j in range(n):
        visited = [0] * n
        ans[i][j] = find_ans(i, j)

for i in ans:
    print(*i)