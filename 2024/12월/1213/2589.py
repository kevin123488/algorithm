import sys
sys.stdin = open('input_2589.txt')
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def check_bfs(l_sero, l_garo, target_point, sero, garo):
    q = deque()
    q.append([l_sero, l_garo, 0])
    visited = [[0] * garo for _ in range(sero)]
    visited[l_sero][l_garo] = 1

    while q:
        now_i, now_j, cnt = q.popleft()
        if [now_i, now_j] == target_point:
            return cnt
        for i in range(4):
            next_i = now_i + di[i]
            next_j = now_j + dj[i]
            if 0 <= next_i < sero and 0 <= next_j < garo and visited[next_i][next_j] == 0 and tresure_map[next_i][next_j] == 'L':
                visited[next_i][next_j] = 1
                q.append([next_i, next_j, cnt + 1])
                


def bfs(l_sero, l_garo, land_points, sero, garo):
    # 현 좌표에서 가장 이동거리가 긴 다른 L 좌표까지의 길이를 구하는 함수
    q = deque()
    q.append([l_sero, l_garo])
    max_cnt = 0
    for i in land_points:
        if [l_sero, l_garo] != i:
            temp_ans = check_bfs(l_sero, l_garo, i, sero, garo)
            if temp_ans:
                max_cnt = max(temp_ans, max_cnt)
    
    return max_cnt


sero, garo = map(int, input().split())
tresure_map = [list(input()) for _ in range(sero)]

# 땅에서만 이동 가능, 보물도 땅에서만 묻힐 수 있음
max_length = 0
land_points = []
for i in range(sero):
    for j in range(garo):
        if tresure_map[i][j] == 'L':
            land_points.append([i, j])

# land_points 순회하면서 현재 조회중인 좌표 외 모든 좌표에 대해 이동거리를 계산
for i in land_points:
    l_sero, l_garo = i
    max_length = max(bfs(l_sero, l_garo, land_points, sero, garo), max_length)

print(max_length)