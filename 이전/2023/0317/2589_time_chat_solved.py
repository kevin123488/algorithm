import sys
sys.stdin = open('input2589.txt')
from collections import deque

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(start):
    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True
    q = deque([(start, 0)])
    max_dist = 0
    while q:
        (i, j), dist = q.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 'L':
                visited[ni][nj] = True
                q.append(((ni, nj), dist+1))
                max_dist = max(max_dist, dist+1)
    return max_dist

# L: 욱지, W: 바다
# 상하좌우로 이웃한 육지로만 이동 가능, 한 칸 이동하는데 1시간 걸림
# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
# 한마디로, 특정 지점에서 특정 지점까지 이동하는데 걸리는 최단시간중 가장 긴 시간을 출력하는 문제

N, M = map(int, sys.stdin.readline().split()) # N: 세로, M: 가로
arr = []
for i in range(N):
    arr.append(list(sys.stdin.readline()))

# 모든 육지에서 bfs 실행
dist = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            dist.append(bfs((i, j)))

# dist 리스트에서 최댓값 찾기
max_dist = max(dist)
# 최단거리로 가장 먼 육지 두 곳 사이의 거리가 정답
print(max_dist)