import sys
sys.stdin = open('input_2573.txt')
from pprint import pprint
sys.setrecursionlimit(100000)
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def check_ving_ha(i, j):
    # visited[i][j] = 1
    # ving_ha의 갈라짐을 판별하는 함수
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ving_ha[ni][nj] != 0 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            check_ving_ha(ni, nj)

n, m = map(int, input().split())
ving_ha = [list(map(int, input().split())) for _ in range(n)]

# 2가지 부분으로 나뉘어야 함
# 1. 빙하가 녹는 부분 -> 구현현
# 2. 빙하가 2개 이상으로 나뉘었는지 확인하는 부분 -> 그래프 탐색

# 빙하를 계속 녹이자
cnt = 0
while True:
    cnt += 1
    ving_ha_melt_cnt = [[0] * m for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if ving_ha[i + 1][j] == 0:
                ving_ha_melt_cnt[i][j] += 1 # 인접한 곳에 0 있으면 빙하 녹임 카운트 증가. 나중에 이 값 ving_ha에서 빼줄거임
            if ving_ha[i - 1][j] == 0:
                ving_ha_melt_cnt[i][j] += 1
            if ving_ha[i][j + 1] == 0:
                ving_ha_melt_cnt[i][j] += 1
            if ving_ha[i][j - 1] == 0:
                ving_ha_melt_cnt[i][j] += 1
    
    
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            ving_ha[i][j] -= ving_ha_melt_cnt[i][j]
            if ving_ha[i][j] < 0:
                ving_ha[i][j] = 0

    visited = [[0] * m for _ in range(n)]
    ving_ha_cnt = 0
    
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if ving_ha[i][j] != 0 and visited[i][j] == 0:
                visited[i][j] = 1
                ving_ha_cnt += 1
                check_ving_ha(i, j)

    
    if ving_ha_cnt == 0:
        print(0)
        break
    elif ving_ha_cnt > 1:
        print(cnt)
        break