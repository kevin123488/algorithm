import sys
sys.stdin = open('input_7576.txt')
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs():
    q = deque()
    max_tomato = 0
    for i in range(n):
        for j in range(m):
            if tomato_box[i][j] == 1:
                max_tomato += 1
                q.append([i, j, 0])
            elif tomato_box[i][j] == 0:
                max_tomato += 1
    
    while q:
        now_i, now_j, days = q.popleft()
        for i in range(4):
            ni = now_i + di[i]
            nj = now_j + dj[i]
            if 0 <= ni < n and 0 <= nj < m and tomato_box[ni][nj] == 0:
                q.append([ni, nj, days + 1])
                tomato_box[ni][nj] = 1
    
    check_tomato = 0
    for i in range(n):
        for j in range(m):
            if tomato_box[i][j] == 1:
                check_tomato += 1
    
    if check_tomato == max_tomato:
        return days
    else:
        return -1

m, n = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(n)]

print(bfs())