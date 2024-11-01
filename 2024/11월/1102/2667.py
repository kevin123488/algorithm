import sys
sys.stdin = open('input_2667.txt')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(sero, garo, cnt):
    visited[sero][garo] = 1
    for i in range(4):
        ni = sero + di[i]
        nj = garo + dj[i]
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and house_board[ni][nj] == 1:
            cnt = dfs(ni, nj, cnt + 1)
    
    return cnt

n = int(input())
house_board = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

danji_num = 0
danji_state = []
for i in range(n):
    for j in range(n):
        if house_board[i][j] == 1 and visited[i][j] == 0:
            danji_num += 1
            visited[i][j] = 1
            cnt = dfs(i, j, 1)
            danji_state.append(cnt)

print(danji_num)
danji_state.sort()
for i in danji_state:
    print(i)