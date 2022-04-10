import sys
from collections import deque

sys.stdin = open('7576.txt')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs():
    while que:
        x, y, cnt = que.popleft()
        # 만약 arr에 0이 없다면? -> 모든 토마토가 다 익은 것 이므로 멈추자
        # flag = 0
        # for k in arr: # arr내의 리스트들을 조회하며
        #     if 0 in k: # 만약 리스트 내에 0이 존재한다면? 아직 덜 익은 토마토가 있다는 뜻이므로
        #         flag = 1 # flag값을 바꿔주자
        # if flag == 0: # flag값이 0이다? 리스트 내에 0이 없다!
        #     return cnt
        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj] != -1:
                que.append((ni, nj, cnt+1))
                visited[ni][nj] = 1
                arr[ni][nj] = 1
    flag = 0
    for k in arr:  # arr내의 리스트들을 조회하며
        if 0 in k:  # 만약 리스트 내에 0이 존재한다면? 아직 덜 익은 토마토가 있다는 뜻이므로
            flag = 1  # flag값을 바꿔주자
    if flag == 0:  # flag값이 0이다? 리스트 내에 0이 없다!
        return cnt
    else:
        return -1

M, N = map(int, input().split()) # M: 열, N: 행
arr = [list(map(int, input().split())) for _ in range(N)] # 토마토의 정보

# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸
# 보관 후 하루가 지나면 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은
# 익은 토마토의 영향을 받아 익게 됨 (상하좌우의 토마토만)

# bfs 쓰자
visited = [[0]*M for _ in range(N)]
# 1인 곳을 순회하며 주변 칸들을 1로 바꿔주자
# 1인 곳의 좌표를 que에 담고 하나씩 빼면서 주변 좌표들의 값을 1로 바꾼 후 que에 담으면?
que = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que.append((i, j, 0))
            visited[i][j] = 1
ans = bfs()
print(ans)