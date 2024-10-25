import sys
sys.stdin = open('1012.txt')
sys.setrecursionlimit(1000000)

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 배추 군집 개수 세는 함수
def dfs(sero, garo, bechu_num):
    visited[sero][garo] = 1
    for i in range(4):
        ni = sero + di[i]
        nj = garo + dj[i]
        if 0 <= ni < n and 0 <= nj < m and ground[ni][nj] == 1 and visited[ni][nj] == 0:
            dfs(ni, nj, bechu_num + 1)
    
    return bechu_num


# input값
t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())

    # 탐색할 밭 만들기
    ground = [[0] * m for _ in range(n)]

    # 배추 위치 입력
    for i in range(k):
        garo, sero = map(int, input().split())
        ground[sero][garo] = 1

    # dfs 활용하여 배추 군집 개수 파악
    visited = [[0] * m for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, 0) # 각각 세로, 가로, 배추 개수
                answer += 1

    print(answer)