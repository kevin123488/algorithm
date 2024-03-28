import sys
from collections import deque
sys.stdin = open('input2206.txt')
input = sys.stdin.readline

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs():
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0))

    while q:
        i, j, w = q.popleft()

        if i == n-1 and j == m-1:
            return visited[i][j][w]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            # 벽을 부순 적이 없을 경우
            if arr[ni][nj] == 0 and visited[ni][nj][w] == 0:
                visited[ni][nj][w] = visited[i][j][w] + 1
                q.append((ni, nj, w))

            # 벽을 부순 적이 있을 경우
            if w == 0 and arr[ni][nj] == 1 and visited[ni][nj][1] == 0:
                visited[ni][nj][1] = visited[i][j][w] + 1
                q.append((ni, nj, 1))

    return -1


# n * m 행렬. 맵에서 0은 이동 가능한 길, 1은 이동 불가한 벽.
# (1, 1)에서 (n, m)까지 이동. 최단 경로로 이동.
# 이동하는 도중 한 개의 벽을 부수고 이동하는게 유리하다면? 벽을 최대 1개까지 부수고 이동 가능.
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하자

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

print(bfs())
