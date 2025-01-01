import sys
sys.stdin = open('1520.txt')
from collections import deque

def bfs(m, n):
    q = deque()
    q.append([0, 0]) # 시작점 넣어주기

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    while q:
        now_i, now_j = q.popleft()
        for i in range(4):
            ni = now_i + di[i]
            nj = now_j + dj[i]
            if 0 <= ni < m and 0 <= nj < n and road_map[now_i][now_j] > road_map[ni][nj]:
                q.append([ni, nj])
                dp[ni][nj] += 1

m, n = map(int, input().split()) # m: 세로, n: 가로
road_map = [list(map(int, input().split())) for _ in range(m)]

# 상하좌우로만 이동 가능
# 0, 0에서 시작하여 m-1, n-1까지 이동하는 경우의 수 출력
# 단 숫자가 높은 칸에서 낮은 칸으로의 이동만 허용됨

dp = [[0] * n for _ in range(m)]
# bfs 하면서 특정 칸에 도달할 때 마다 새로운 경로로 도달하였으면 dp에 + 1 해주자

bfs(m, n)
print(dp[m-1][n-1])