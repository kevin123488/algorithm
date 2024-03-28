import sys
sys.stdin = open('input2589.txt')
from collections import deque

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(info, ans): # [[0, 1], [0, 2], 0], 0
    start, fin, cnt = info
    visited = [[0] * M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    q = deque()
    q.append([start, cnt])
    while q:
        start_point = q.popleft()
        # [[0, 1], 0]
        if start_point[0] == fin:
            if ans > start_point[1]:
                return ans
            else:
                return start_point[1]
        for i in range(4):
            ni = start_point[0][0] + di[i]
            nj = start_point[0][1] + dj[i]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 'L':
                visited[ni][nj] = 1
                q.append([[ni, nj], start_point[1] + 1])

    return ans



# L: 욱지, W: 바다
# 상하좌우로 이웃한 육지로만 이동 가능, 한 칸 이동하는데 1시간 걸림
# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
# 한마디로, 특정 지점에서 특정 지점까지 이동하는데 걸리는 최단시간중 가장 긴 시간을 출력하는 문제

N, M = map(int, sys.stdin.readline().split()) # N: 세로, M: 가로
arr = []
for i in range(N):
    arr.append(list(sys.stdin.readline()))

check_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            check_list.append([i, j])

ans = 0
for i in range(len(check_list)-1): # 출발
    for j in range(i+1, len(check_list)): # 도착
        if i != j:
            ans = bfs([check_list[i], check_list[j], 0], ans)
            # [[0, 1], [0, 2], 0], 0

print(ans)