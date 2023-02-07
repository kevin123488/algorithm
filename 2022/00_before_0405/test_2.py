# 1명의 경비원, N*N의 이차원 리스트 주어짐. 통로 0, 벽 1, 경비원 2
# 경비원은 상하좌우 감시, 감시 거리는 무한. 통로에 배치됨
# 경비원의 눈길이 닿지 않는다? 사각지대. 이러한 사각지대의 개수를 출력하면 되는 문제.
# 통로의 폭은 항상 1이다. 경비원이 감시할 수 있는 영역은 자신의 위치를 포함하여 상하좌우로 벽을 만나기 전까지 통로이다.
import sys
sys.stdin = open('test.txt')

T = int(input()) # 테스트 케이스의 수
for tc in range(1, T+1):
    N = int(input()) # 이차원 리스트 한 변의 길이
    arr = [list(map(int, input().split())) for _ in range(N)] # 이차원 리스트 받아옴

    total_cnt = 0 # 감시 대상이 되는 모든 구간의 수
    start = [] # 경비원이 서있는 곳
    cnt_1 = 0 # 경비원이 감시 가능한 윗구간
    cnt_2 = 0 # 아랫구간
    cnt_3 = 0 # 왼쪽구간
    cnt_4 = 0 # 오른쪽구간

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                total_cnt += 1
            elif arr[i][j] == 2:
                start += [i, j]

    di = [-1, 1, 0, 0] # 상하좌우
    dj = [0, 0, -1, 1] # 상하좌우
    ii = start[0] # 경비원이 있는 곳의 i행
    jj = start[1] # 경비원이 있는 곳의 j행

    ni = 0
    nj = 0

    for a in range(N): # 각 방향당 N칸 이상을 조회할 수 없음
        ni = ii + a*di[0]
        nj = jj + a*dj[0]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                cnt_1 += 1
            elif arr[ni][nj] == 1:
                break
        else:
            break

    for a in range(N): # 각 방향당 N칸 이상을 조회할 수 없음
        ni = ii + a*di[1]
        nj = jj + a*dj[1]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                cnt_2 += 1
            elif arr[ni][nj] == 1:
                break
        else:
            break

    for a in range(N): # 각 방향당 N칸 이상을 조회할 수 없음
        ni = ii + a*di[2]
        nj = jj + a*dj[2]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                cnt_3 += 1
            elif arr[ni][nj] == 1:
                break
        else:
            break

    for a in range(N): # 각 방향당 N칸 이상을 조회할 수 없음
        ni = ii + a*di[3]
        nj = jj + a*dj[3]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                cnt_4 += 1
            elif arr[ni][nj] == 1:
                break
        else:
            break

    ans = total_cnt - cnt_1 - cnt_2 - cnt_3 - cnt_4
    print(f'#{tc} {ans}')