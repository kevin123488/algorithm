import sys
sys.stdin = open('input_7576.txt')
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def check_tomato():
    check_ans = 0 # 현시점 익은 토마토 수
    for i in range(n):
        for j in range(m):
            if tomato_box[i][j] == 1:
                check_ans += 1
    
    if check_ans == max_tomato: # 익을거 다 익었으면
        return 'finish'
    else: # 다 안익었으면 지금까지 익은 토마토 수 리턴
        return check_ans
    
def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if tomato_box[i][j] == 1:
                q.append([i, j, 1])
    
    while q:
        now_i, now_j, cnt_var = q.popleft()
        if cnt_var == 2:
            break
        for i in range(4):
            ni = now_i + di[i]
            nj = now_j + dj[i]
            if 0 <= ni < n and 0 <= nj < m and tomato_box[ni][nj] == 0:
                tomato_box[ni][nj] = 1
                q.append([ni, nj, 2])


m, n = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(n)]
max_tomato = 0
for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 0 or tomato_box[i][j] == 1:
            max_tomato += 1
# 0은 익지 않은 토마토, 1은 익은 토마토, -1은 토마토가 없는 칸
# 익은 토마토는 하루가 지나면 자신 기준 상, 하, 좌, 우에 위치한 토마토를 익게 함
# tomato_box에 있는 모든 토마토가 익는데 걸리는 최소 시간을 구하자. 만일 모두 익을 수 없다면 -1을 출력

# 1인 좌표를 모두 넣어두고, 그 좌표를 하나씩 꺼내며 상하좌우 1씩 추가하자
# 그러기 위해선 토마토가 모두 익었는지 아닌지를 체크해야 함
# 익을 수 있는 토마토의 수 최댓값 (n * m - (-1개수))을 충족하는 최소 횟수를 리턴
# 만약 최댓값을 달성하지 못했는데 2회 연속 같은 수가 나왔다면 -1 리턴
# 필요한 함수: check_tomato(익은 토마토 수를 체크한 후 비교 결과를 리턴하는 함수)

before_check = 0
cnt = 0
while True:
    x = check_tomato()
    if x == 'finish':
        print(cnt)
        break
    elif x == before_check: # 다 안익었는데 이전 회차와 익은 토마토 수가 같다면 더 이상 익힐 수 없음
        print(-1)
        break
    else: # 다 안익었으며 이전회차와 달라진게 있다면
        cnt += 1 # 다음날로 이동하고
        before_check = x # 이전 체크 결과 갱신해주자
        bfs()