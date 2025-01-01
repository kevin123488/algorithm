import sys
sys.stdin = open('1520.txt')

def dfs(a, b, m, n):
    if a == m - 1 and b ==  n - 1:
        return 1
    
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    if dp[a][b] != -1:
        return dp[a][b]

    cnt = 0
    for i in range(4):
        ni = a + di[i]
        nj = b + dj[i]
        if 0 <= ni < m and 0 <= nj < n and road_map[a][b] > road_map[ni][nj]:
            cnt += dfs(ni, nj, m, n)
    
    dp[a][b] = cnt
    return dp[a][b] # 이 dfs 함수는 a, b위치로 이동하는 가짓수를 리턴하는 함수임


m, n = map(int, input().split()) # m: 세로, n: 가로
road_map = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

# 상하좌우로만 이동 가능
# 0, 0에서 시작하여 m-1, n-1까지 이동하는 경우의 수 출력
# 단 숫자가 높은 칸에서 낮은 칸으로의 이동만 허용됨

print(dfs(0, 0, m, n))