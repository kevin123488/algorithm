import sys
sys.stdin = open('input_2667.txt')
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(height, width, answer):
    q = deque()
    q.append([height, width])
    visited[height][width] = 1

    while q:
        now_h, now_w = q.popleft()
        answer += 1
        # visited[now_h][now_w] = 1
        for i in range(4):
            ni = now_h + di[i]
            nj = now_w + dj[i]
            if 0 <= ni < n and 0 <= nj < n and house_list[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj])
    
    return answer

n = int(input())
house_list = [list(map(int, input())) for _ in range(n)]

danji_num = []
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if house_list[i][j] == 1 and visited[i][j] == 0:
            danji_num.append(bfs(i, j, 0))

print(len(danji_num))
danji_num.sort()
for i in danji_num:
    print(i)