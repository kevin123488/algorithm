import sys
sys.stdin = open('input_2667.txt')
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(sero, garo, cnt):
    q = deque()
    q.append([sero, garo, cnt])
    visited[sero][garo] = 1

    while q:
        now_i, now_j, now_cnt = q.popleft()

        for i in range(4):
            ni = now_i + di[i]
            nj = now_j + dj[i]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and house_board[ni][nj] == 1:
                visited[ni][nj] = 1
                now_cnt += 1
                q.append([ni, nj, now_cnt])
    
    return now_cnt

n = int(input())
house_board = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

danji_num = 0
danji_list = []
for i in range(n):
    for j in range(n):
        if house_board[i][j] == 1 and visited[i][j] == 0:
            danji_num += 1
            danji_list.append(bfs(i, j, 1))

print(danji_num)
danji_list.sort()
for i in danji_list:
    print(i)