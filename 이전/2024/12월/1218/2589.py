import sys
sys.stdin = open('input_2589.txt')
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited = [[100000] * garo for _ in range(sero)]
    visited[i][j] = 0
    cnt = 0

    while q:
        now_i, now_j = q.popleft()
        for i in range(4):
            next_i, next_j = now_i + di[i], now_j + dj[i]
            if 0 <= next_i < sero and 0 <= next_j < garo and visited[now_i][now_j] + 1 < visited[next_i][next_j] and map_list[next_i][next_j] == 'L':
                q.append([next_i, next_j])
                visited[next_i][next_j] = visited[now_i][now_j] + 1
    
    for i in range(sero):
        for j in range(garo):
            if visited[i][j] != 100000:
                cnt = max(cnt, visited[i][j])
    
    return cnt

    

sero, garo = map(int, input().split())
map_list = [list(input()) for _ in range(sero)]

answer = 0
for i in range(sero):
    for j in range(garo):
        if map_list[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)