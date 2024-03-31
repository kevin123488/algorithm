def dfs(visited, i, n, computers):
    visited[i] = 1
    for j in range(n):
        if computers[i][j] == 1 and visited[j] == 0:
            dfs(visited, j, n, computers)


def solution(n, computers):
    answer = 0
    # 네트워크(연결되어있는 덩어리)의 수 리턴
    # n개의 컴퓨터, 컴퓨터는 0번부터 n - 1번까지 있음
    # computers[a][b] -> a번 컴퓨터와 b번 컴퓨터의 연결 유무(연결1, 연결안됨0)
    
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            dfs(visited, i, n, computers)
    
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))