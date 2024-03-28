# N, M이 주어짐
# 1~N까지의 자연수 중 중복 없이 M개를 고른 수열
def dfs(a, M):
    visited[a] = 1:
    

N, M = map(int, input().split())

visited = [0]*N
dfs(0, M) 