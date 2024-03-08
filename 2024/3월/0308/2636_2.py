import sys
sys.stdin = open('2636.txt')
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append([0, 0])
    cnt = 0
    visited[0][0] = 1
    while q:
        i, j = q.popleft()
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < height and 0 <= nj < width and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                if cheese[ni][nj] == 0:
                    q.append([ni, nj])
                else:
                    cheese[ni][nj] = 0
                    cnt += 1

    return cnt


height, width = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(height)]

# 0, 0에서 시작해서 bfs를 돌면
# 치즈에 둘러쌓인 공기 부분은 스킵이 가능

ans_list = []
while True:
    visited = [[0] * width for _ in range(height)]
    ans = bfs()
    if ans == 0:
        break
    else:
        ans_list.append(ans)

print(len(ans_list), ans_list[-1])