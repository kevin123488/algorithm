import sys
sys.stdin = open('input_1261.txt')
from collections import deque

def bfs(m, n):
    q = deque()
    q.append([0, 0]) # 첫 시작점의 세로, 가로 좌표
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    visited[0][0] = 0

    while q:
        now_i, now_j = q.popleft()

        for i in range(4):
            ni = now_i + di[i]
            nj = now_j + dj[i]
            if 0 <= ni < n and 0 <= nj < m:
                if miro[ni][nj] == 0 and visited[ni][nj] > visited[now_i][now_j]:
                    visited[ni][nj] = visited[now_i][now_j]
                    q.append([ni, nj])
                if miro[ni][nj] == 1 and visited[ni][nj] > visited[now_i][now_j] + 1:
                    visited[ni][nj] = visited[now_i][now_j] + 1
                    q.append([ni, nj])
    
    return visited[n - 1][m - 1]

m, n = map(int, input().split()) # m 가로, n 세로
miro = [list(map(int, input())) for _ in range(n)]

# print(m, n, miro)

visited = [[10009] * m for _ in range(n)]
print(bfs(m, n))