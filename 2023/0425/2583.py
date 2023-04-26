import sys
from collections import deque
sys.stdin = open('input2583.txt')
input = sys.stdin.readline

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(i, j): # i는 세로, j는 가로 값
    q = deque()
    visited[i][j] = 1
    q.append([i, j])
    cnt = 1
    while q:
        now_i, now_j = q.popleft()
        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if 0 <= ni < m and 0 <= nj < n and visited[ni][nj] == 0 and ans_list[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj])
                cnt += 1

    return cnt

# 눈금 간격 1인 m * n 크기의 모눈종이가 있음
# 이 모눈종이 위의 눈금에 맞추어 k개의 직사각형을 그릴 때, k개의 직사각형 내부를 제외한 나머지 부분이
# 몇 개의 분리된 영역으로 나뉜다. (색칠되지 않은 부분)
# 몇 개의 분리된 영역으로 나뉘는지와 분리된 영역의 넓이를 오름차순으로 구하여라

m, n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]
# [1, 2]의 경우 [m-1, 2-1]의 형태로 입력됨
ans_list = [[0] * n for _ in range(m)]
for i in arr:
    x1, y1, x2, y2 = i # x는 가로, y는 세로
    y1 = m - y1
    y2 = m - y2
    for j in range(x1, x2):
        for k in range(y2, y1):
            ans_list[k][j] = 1

visited = [[0] * n for _ in range(m)]
ans = []
for i in range(m):
    for j in range(n):
        if ans_list[i][j] == 0 and visited[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
print(*ans)