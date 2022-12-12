import sys
sys.stdin = open('1012input.txt')
sys.setrecursionlimit(10000)

# 배추에 배추흰지렁이가 한 마리라도 살고 있으면? 인접한 다른 배추로 이동 가능.
# 인접하지 않은 배추로는 이동이 불가.
# 몇 개의 단위로 배추밭이 이루어져 있는지를 보는 문제.
# 1은 배추가 심어져 있는 땅, 0은 배추가 심어져있지 않은 땅.

# 델타탐색
di = [1, -1, 0, 0] # 하 상 우 좌
dj = [0, 0, 1, -1]

def dfs(N, M, Nmax, Mmax):
    arr[N][M] = 0 # 방문한 곳은 0 처리해주고
    for i in range(4):
        if 0 <= N + di[i] < Nmax and 0 <= M + dj[i] < Mmax and arr[N + di[i]][M + dj[i]] == 1: # 상하좌우 탐색할 수 있으면서 그 값이 1이면
            dfs(N + di[i], M + dj[i], Nmax, Mmax)
    return

T = int(input())
for i in range(T):
    # 첫 줄: 배추를 심은 배추밭의 가로 길이와 세로 길이, 그리고 심어져있는 위치의 개수(M, N, K)
    # 둘째 줄부터 K개의 줄: 배추의 위치(X, Y)가 주어짐.

    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    # 배추밭의 모양을 받아왔다. 다음은?
    # dfs를 이용, 한큐에 순회 가능한 애들을 체크하자.
    # 아이디어: 밭의 0, 0 지점부터 순회한다. 만약 해당 칸이 1이라면?
    # 그 칸을 dfs 돌리자. dfs 돌리면서 지나는 1로 칠해진 칸은? 지난 후엔 0으로 바꿔주자.
    # 갈 수 있는 칸이 없으면? cnt 1 증가시키고 다음 칸으로 이동해 위 과정 반복.

    cnt = 0 # 몇 개의 배추벌레가 필요한지 세는 값

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1: # 배추벌레 있는 곳 시작
                dfs(i, j, N, M)
                cnt += 1

    print(cnt)