import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('input_1520.txt')

def bfs(m, n):
    visited = [[0] * n for _ in range(m)]
    q = deque()
    q.append([0, 0, height_list[0][0], visited])

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    cnt = 0
    
    while q:
        now_i, now_j, now_height, find_visited = q.popleft()
        semi_visited = deepcopy(find_visited)
        semi_visited[now_i][now_j] =1
        # find_visited[now_i][now_j] = 1
        if now_i == m - 1 and now_j == n - 1:
            cnt += 1
        for i in range(4):
            ni = now_i + di[i]
            nj = now_j + dj[i]
            if  0 <= ni < m and 0 <= nj < n and now_height > height_list[ni][nj] and semi_visited[ni][nj] == 0:
                # visited[ni][nj] = 1
                # find_visited[ni][nj] = 1
                # semi_visited[ni][nj] =1
                q.append([ni, nj, height_list[ni][nj], semi_visited])

    return cnt


m, n = map(int, input().split())
height_list = []
for i in range(m):
    height_list.append(list(map(int, input().split())))

# 상하좌우만 이동 가능
# 각 칸의 숫자가 높이임
# 항상 높이가 더 낮은 곳으로만 이동
# 왼쪽 위에서 오른쪽 아래로 이동할 때 위의 조건을 만족하며
# 완주할 수 있는 가짓수를 구하자

print(bfs(m, n))