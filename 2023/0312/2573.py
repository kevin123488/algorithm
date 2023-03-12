import sys
sys.stdin = open('2573input.txt')
from copy import deepcopy
from collections import deque

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 빙하 주변의 0 갯수를 체크하는 함수
def check_sur(i, j, copy_arr):
    cnt = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m:
            if copy_arr[ni][nj] == 0:
                cnt += 1

    return cnt

# 시간 진행 함수
def life_goes_on(copy_arr):
    check = 0
    # 빙하를 녹이는 함수.
    # arr를 순회하면서 빙하를 녹여야 함. 그럼 앞 빙하가 녹은 결과물이 뒷 빙하의 녹음을 결정하는 데에 영향을 끼칠 수 있음
    # copy_arr를 순회하며 빙하의 녹은 결과는 arr에 저장해줘야 한다.
    for i in range(n):
        for j in range(m):
            melt = check_sur(i, j, copy_arr)
            if arr[i][j] > melt:
                arr[i][j] -= melt
            else:
                arr[i][j] = 0
            if arr[i][j] == 0:
                check += 1

    if check == n*m: # 모든 칸이 0일 경우 -> 빙하가 다 녹은 것
        return 0
    else:
        return 1
    # 1년 진행 완료

def bfs(year): # 빙하가 몇 덩어리로 구성되어 있는지 확인하는 함수
    visited = [[0] * m for _ in range(n)]
    flag = 0
    for i in range(n):
        if flag == 1:
            break
        for j in range(m):
            if arr[i][j] != 0:
                q.append([i, j])
                visited[i][j] = 1
                flag = 1
                break

    while q:
        start = q.popleft()
        for i in range(4):
            ni = start[0] + di[i]
            nj = start[1] + dj[i]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] != 0:
                visited[ni][nj] = 1
                q.append([ni, nj])

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and arr[i][j] != 0:
                return year
    return 0


# 시작 함수
def start():
    year = 0
    while True:
        # print(arr)
        year += 1
        copy_arr = deepcopy(arr)
        if life_goes_on(copy_arr) == 0: # arr가 녹은 상태로 갱신되어 있을 것
            return 0
        copy_arr = arr # 다음 탐색을 대비, copy_arr를 arr와 맞춰주어야 함
        if bfs(year) == year:
            return year



n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 빙산의 정보가 이차원 리스트에 저장됨
# 빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장됨
# 빙산 이외의 바다에 해당되는 칸에는 0이 저장
# 빙산의 높이는 1년당 해당 칸과 접해있는 0칸의 수만큼 줄어듦. 0보다 더 줄어들지는 않는다.
# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성
# 빙산이 전부 녹을때 까지 두 덩어리 이상으로 분리되지 않는다? -> 0 출력

# 1. 1년단위로 시간을 진행시키며 빙하를 녹인다
# 2. 빙하가 녹은 후 bfs를 이용해 몇 개의 덩어리가 존재하는지 확인
# 3. 2개 이상의 빙하 덩어리가 발견되면 함수 종료하고 몇 년이 지났는지 출력
# 4. 빙하가 모두 녹아 0으로 가득 찬 리스트를 순회할 경우 함수 종료하고 0 출력
copy_arr = deepcopy(arr) # 이 copy_arr는 해당 년도가 진행될 때의 시점을 freeze 해둔 것
q = deque()
print(start())