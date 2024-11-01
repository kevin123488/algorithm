import sys
sys.stdin = open('input_2667.txt')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(height, width, answer):
    visited[height][width] = 1
    answer += 1
    for i in range(4):
        ni = height + di[i]
        nj = width + dj[i]
        if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and house_list[ni][nj] == 1:
            answer = dfs(ni, nj, answer)
    
    return answer

n = int(input())
house_list = [list(map(int, input())) for _ in range(n)]

danji_num = []
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if house_list[i][j] == 1 and visited[i][j] == 0: # 집이 있으며 아직 방문하지 않았을 때
            answer = 0
            danji_num.append(dfs(i, j, answer))

danji_num.sort()
print(len(danji_num))
for i in danji_num:
    print(i)