import sys
sys.stdin = open('test.txt')

T = int(input()) # 테스트 케이스의 수
for tc in range(1, T+1):
    N = int(input()) # 이차원 리스트 한 변의 길이
    arr = [list(map(int, input().split())) for _ in range(N)] # 이차원 리스트 받아옴

    total_cnt = 0 # 감시 대상이 되는 모든 구간의 수
    start = [] # 경비원이 서있는 곳
    cnt = 0 # 경비원이 감시 가능한 구간

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

    for k in range(4): # 각 방향당 N칸 이상을 조회할 수 없음
        for a in range(N):
            ni = ii + a*di[k]
            nj = jj + a*dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    cnt += 1
                elif arr[ni][nj] == 1:
                    break
            else:
                break


    ans = total_cnt - cnt
    print(f'#{tc} {ans}')