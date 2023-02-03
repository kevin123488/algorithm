import sys
sys.stdin = open('16234input.txt')
from collections import deque

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(k, l):
    global flag
    count = 1
    plus = arr[k][l]
    # beonghaped[k][l] = 1
    beonghaped.append([k, l])
    visited[k][l] = 1
    while queue:
        start = queue.popleft()
        for i in range(4):
            ni = start[0] + di[i]
            nj = start[1] + dj[i]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0: # 범위 내에 있으면서 아직 방문하지 않았다면
                if L <= ((arr[start[0]][start[1]] - arr[ni][nj]) ** 2) ** (1/2) <= R and [ni, nj] not in beonghaped:
                    count += 1
                    plus += arr[ni][nj]
                    # beonghaped[ni][nj] = 1
                    beonghaped.append([ni, nj])
                    visited[ni][nj] = 1
                    queue.append([ni, nj, arr[ni][nj]])
                    flag = 1 # 병합 요소가 추가로 있으면 flag값을 1로 바꾸자

    return count, plus

N, L, R = map(int, input().split())
# 국가간의 인구 수 분포
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# 병합 가능한 국가의 모든 국경선을 열어두어야 한다.
queue = deque()
visited = [[0] * N for _ in range(N)]
# beonghaped = [[0] * N for _ in range(N)] # 병합 유무 판단
beonghaped = [] # 병합 대상이 되는 좌표들을 넣어줄 것

# 덩어리를 바꿔주는 역할
flag = 1
ans = 0
while flag:
    flag = 0
    ans += 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0: # 아직 탐색하지 않은 덩어리라면
                queue.append([i, j, arr[i][j]])
                # bfs() # 지금 상태면 병합 가능한 애들을 모두 한번에 합쳐버림
                # 이거 한번 돌때마다 한 덩어리에 대한 병합 가능 여부가 판단됨. 그 때 병합 가능한 칸의 정보를 받고, 그 칸들의 값의 합과 칸의 수를 받아 사용해야 할 것 같다.
                count, plus = bfs(i, j)
                # 4중 for문인데 이거 맞나... 라기엔 이중 포문 내의 bfs와 시간 복잡도가 같기 때문에 괜찮을 것 같다.
                # for k in range(N):
                #     for z in range(N):
                #         if beonghaped[k][z] == 1: # 병합 대상이면
                #             arr[k][z] = plus // count
                for k in beonghaped:
                    arr[k[0]][k[1]] = plus // count

                # beonghaped = [[0] * N for _ in range(N)] # 한 덩어리 병합 끝났으면 병합 정보 초기화 해야 함
                beonghaped = []
    visited = [[0] * N for _ in range(N)]

print(ans - 1) # 최초 실행시 병합 요소가 없더라도 한번은 더해지기 때문에, 1을 빼주어야 한다.