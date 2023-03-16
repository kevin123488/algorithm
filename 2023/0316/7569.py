import sys
sys.stdin = open('input7569.txt')
from collections import deque

# 이차원 리스트를 겹겹이 쌓은 형태로 보관함을 만든다
# 보관함에는 토마토가 보관되어 있다. 보관 후 하루가 지나면 익은 토마토들의 인접한
# 위치에 위채한(위, 아래, 앞, 뒤, 좌, 우) 토마토들은 익은 토마토의 영향을 받아 익게 된다
# 창고에 보관된 토마토가 며칠이 지나야 다 익는지 그 최소 일수를 구해보자
# 익은 토마토: 1, 익지 않은 토마토: 0, 토마토가 있지 않은 칸: -1

# 델타탐색
# 상, 하, 좌, 우, 위, 아래
di = [0, 0, 0, 0, -1, 1]
dj = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, -1, 1, 0, 0]

def bfs(to_cnt):
    while q:
        start = q.popleft()
        visited[start[0]][start[1]][start[2]] = 1
        for i in range(6):
            ni = start[0] + di[i]
            nj = start[1] + dj[i]
            nz = start[2] + dz[i]
            if 0 <= ni < H and 0 <= nj < N and 0 <= nz < M and visited[ni][nj][nz] == 0 and arr[ni][nj][nz] == 0:
                to_cnt -= 1
                arr[ni][nj][nz] = 1
                q.append([ni, nj, nz, start[3] + 1])
                if to_cnt == 0:
                    return start[3] + 1

    if to_cnt != 0:
        return -1

M, N, H = map(int, input().split()) # M, N: 토마토 들어있는 각 층의 가로와 세로, H: 쌓아지는 층
arr = []
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, input().split())))
    arr.append(temp)

# arr[x][y][z]
# x: 몇 층인지 확인
# y: 각 층에서 몇 번째 세로줄인지 확인
# z: 각 층에서 몇 번째 가로줄인지 확인
# bfs 사용
# 익어있는 토마토가 들어있는 칸의 정보를 q에 집어넣자
q = deque()
visited = [[[0] * M for _ in range(N)] for __ in range(H)]
to_cnt = 0
for i in range(H):
    for j in range(N):
        for z in range(M):
            if arr[i][j][z] != -1: # 토마토 수 체크
                to_cnt += 1
                if arr[i][j][z] == 1:
                    to_cnt -= 1
                    q.append([i, j, z, 0])

if to_cnt == 0:
    print(0)
else:
    print(bfs(to_cnt))