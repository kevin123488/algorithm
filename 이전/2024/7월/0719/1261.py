import sys
sys.setrecursionlimit(10000000)
sys.stdin = open('input_1261.txt')

def dfs(m, n, visited, semi_answer, now_i, now_j):
    global answer

    if semi_answer >= answer: # 탐색중인 루트에서 부순 벽의 수가 현재 answer보다 클 경우 유망성조사에서 out
        return
    
    if now_i == n - 1 and now_j == m - 1:
        if semi_answer < answer:
            answer = semi_answer
            return
        else:
            return

    for i in range(4):
        ni = now_i + di[i]
        nj = now_j + dj[i]

        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
            if miro[ni][nj] == 0:
                visited[ni][nj] = 1
                dfs(m, n, visited, semi_answer, ni, nj)
                visited[ni][nj] = 0

            elif miro[ni][nj] == 1:
                # semi_answer += 1
                visited[ni][nj] = 1
                # miro[ni][nj] = 0
                dfs(m, n, visited, semi_answer + 1, ni, nj)
                # miro[ni][nj] = 1
                visited[ni][nj] = 0
                # semi_answer -= 1



# 알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 
# 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.
# 알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 
# 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 
# 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 
# 단, 미로의 밖으로 이동 할 수는 없다.
# 벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 
# 벽을 부수면, 빈 방과 동일한 방으로 변한다.
# 만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 
# 안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.
# 현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 
# 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

m, n = map(int, input().split()) # m 가로, n 세로
miro = [list(map(int, input())) for _ in range(n)]

# print(m, n, miro)
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 모든 루트 확인, 부수는 벽 개수 체크하여 비교
visited = [[0] * m for _ in range(n)]
answer = 1000000
dfs(m, n, visited, 0, 0, 0)

print(answer)