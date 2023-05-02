import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('input2468.txt')
input = sys.stdin.readline

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(i, j, visited, land):
    q = deque()
    q.append([i, j])
    while q:
        now_i, now_j = q.popleft()
        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and land[ni][nj] != 0:
                visited[ni][nj] = 1
                q.append([ni, nj])

    return visited

def find_ans(rain, land, visited):
    # 물에 잠긴 부분을 0으로 바꾸어주자
    # 그 후 그래프를 탐색하여 몇 개의 덩어리로 이루어져 있는지 확인하자
    for i in range(n):
        for j in range(n):
            if land[i][j] <= rain:
                land[i][j] = 0

    # 그래프 탐색 시작점 찾기
    cnt = 0
    for i in range(n):
        for j in range(n):
            if land[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                visited[i][j] = 1
                visited = bfs(i, j, visited, land)

    return cnt

# 지역의 높이 정보를 파악한다.
# 많은 비가 내렸을 때, 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어지는지 조사
# 내리는 비의 양에 따라 일정 높이 이하의 땅은 모두 물에 잠긴다.
# 장마철에 물에 잠기지 않는 안전한 영역의 덩어리의 최대 수를 구하여보자.

n = int(input())
land = []
max_land = 0
for i in range(n):
    line = list(map(int, input().split()))
    land.append(line)
    max_land = max(max(line), max_land)


ans = 1
for i in range(1, max_land + 1):
    # find_ans 함수는
    visited = [[0] * n for _ in range(n)]
    land_copy = deepcopy(land)
    ans = max(find_ans(i, land_copy, visited), ans)

print(ans)