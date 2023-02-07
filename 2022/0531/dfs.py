# dfs 리마인드
# 기본적인 미로탐색 문제

import sys
sys.stdin = open('dfs.txt')

# 델타 탐색
di = [1, -1 ,0, 0]
dj = [0, 0, 1, -1]

def dfs(a, b, g):
    global N, M, how_long
    visited[a][b] = 1

    if how_long < g:
        return

    if a == N-1 and b == M-1:
        if how_long > g:
            how_long = g
        return
    
    for i in range(4):
        ni = a + di[i]
        nj = b + dj[i]

        if 0 <= ni <= N-1 and 0 <= nj <= M-1 and visited[ni][nj] == 0 and arr[ni][nj] == 1: # 범위 내면서 아직 방문하지 않았으면
            dfs(ni, nj, g+1)
            visited[ni][nj] = 0


# 1은 이동 가능한 칸, 0은 이동 불가능한 칸
# (1, 1)에서 출발, (N, M)으로 이동
# 그 때 지나야하는 최소의 칸 수는?
# 이동시 인접한 칸으로만 이동 가능

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
how_long = 10000000000

dfs(0, 0, 0) # 시작점의 좌표 a, b, 이동 칸 수
print(how_long+1)