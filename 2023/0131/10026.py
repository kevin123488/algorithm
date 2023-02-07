import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('10026input.txt')

# 델타 탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs():
    while queue:
        start = queue.popleft()
        for i in range(4):
            ni = start[0] + di[i]
            nj = start[1] + dj[i]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == start[2]: # 다음 탐색할 곳이 범위 안에 있으며 방문하지 않았다면
                queue.append([ni, nj, arr[ni][nj]])
                visited[ni][nj] = 1 # 방문체크 해줘야 다시 안 감

def bfs2():
    while queue2:
        start = queue2.popleft()
        for i in range(4):
            ni = start[0] + di[i]
            nj = start[1] + dj[i]
            if 0 <= ni < N and 0 <= nj < N and visited2[ni][nj] == 0 and arr2[ni][nj] == start[2]: # 다음 탐색할 곳이 범위 안에 있으며 방문하지 않았다면
                queue2.append([ni, nj, arr2[ni][nj]])
                visited2[ni][nj] = 1 # 방문체크 해줘야 다시 안 감

N = int(input())
arr = [] # 그림 원본
for i in range(N):
    arr.append(list(input()))

arr2 = deepcopy(arr) # 적록색약이 보는 그림
for i in range(N):
    for j in range(N):
        if arr2[i][j] == 'G':
            arr2[i][j] = 'R' # 적록색약이 보는 그림을 만들어주자

# bfs 사용
# 너비 우선 탐색임. 어떻게 돌려야 할까?

visited = [[0] * N for _ in range(N)] # 방문기록 체크
visited2 = [[0] * N for _ in range(N)] # 적록색약 방문기록 체크
queue = deque() # 큐
queue2 = deque() # 적록색약 큐
ans_non = 0 # 구획
ans = 0 # 적록색약의 구획

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0: # 아직 방문하지 않았으면 그 점을 기점으로 bfs 돌자
            queue.append([i, j, arr[i][j]])
            ans_non += 1
            bfs()

for i in range(N):
    for j in range(N):
        if visited2[i][j] == 0: # 아직 방문하지 않았으면 그 점을 기점으로 bfs 돌자
            queue2.append([i, j, arr2[i][j]])
            ans += 1
            bfs2()

print(ans_non, ans)