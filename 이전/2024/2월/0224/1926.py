# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
# 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
# 그림의 넓이란 그림에 포함된 1의 개수이다.

import sys
from collections import deque
sys.stdin = open('1926.txt')

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    picture[i][j] = 0
    size = 1
    while q:
        a, b = q.popleft()
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < m and picture[ni][nj] == 1 and visited[ni][nj] == 0:
                size += 1
                visited[ni][nj] = 1
                q.append([ni, nj])
    
    return size

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# bfs 탐색으로 풀어보자

group_num = 0
ans = 0
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and visited[i][j] == 0:
            group_num += 1
            ans = max(bfs(i, j), ans)

print(group_num, ans)