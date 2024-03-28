import sys
from collections import deque
sys.stdin = open('input2206.txt')
input = sys.stdin.readline

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(i, j, ans):
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    arr[i][j] = 0
    q = deque()
    cnt = 1
    q.append([0, 0, cnt])
    while q:
        now_i, now_j, now_cnt = q.popleft()
        if now_i == n-1 and now_j == m-1:
            ans = now_cnt
            break
        if now_cnt > ans:
            break
        visited[now_i][now_j] = 1
        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj, now_cnt + 1])

    return ans


# n * m 행렬. 맵에서 0은 이동 가능한 길, 1은 이동 불가한 벽.
# (1, 1)에서 (n, m)까지 이동. 최단 경로로 이동.
# 이동하는 도중 한 개의 벽을 부수고 이동하는게 유리하다면? 벽을 최대 1개까지 ㅜ수고 이동 가능.
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하자

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
ans = 10 ** 10
ans = min(bfs(0, 0, ans), ans)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            visited = [[0] * m for _ in range(n)]
            ans = min(bfs(i, j, ans), ans)
            arr[i][j] = 1

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)