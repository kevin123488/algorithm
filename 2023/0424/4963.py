import sys
sys.stdin = open('input4963.txt')
from collections import deque
input = sys.stdin.readline

# 델타탐색(대각선 포함)
di = [0, 0, 1, -1, 1, 1, -1, -1]
dj = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(i, j, ans):
    q = deque()
    visited[i][j] = 1
    q.append([i, j, ans])
    while q:
        now_i, now_j, now_ans = q.popleft()
        for k in range(8):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                visited[ni][nj] = 1
                q.append([ni, nj, ans])


while True:
    w, h = map(int, input().split()) # w: 너비, h: 높이
    if w == h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)] # 1: 땅, 2: 바다
    # 상하좌우, 대각선으로 이동 가능한 경우 섬이 아님
    ans = 0
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                ans += 1
                bfs(i, j, ans)

    print(ans)