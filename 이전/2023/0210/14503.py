import sys
sys.stdin = open('14503input.txt')
sys.setrecursionlimit(10000000)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def find_clean_blank(r, c, d):
    d = d
    for i in range(5):
        if d == 0: # 북쪽을 바라보고 있다면
            if 0 <= c-1 < M and arr[r][c-1] == 0: # 반시계 방향으로 90도 돌린 서쪽을 바라보고, 그 칸이 청소 가능한 빈 칸이면
                return start_clean(r, c-1, 3) # 해당 칸의 좌표와 서쪽 데이터를 넣은 후 청소 함수 실행
            else:
                d = 3

        elif d == 1:
            if 0 <= r-1 < N and arr[r-1][c] == 0:
                return start_clean(r-1, c, 0)
            else:
                d = 0

        elif d == 2:
            if 0 <= c+1 < M and arr[r][c+1] == 0:
                return start_clean(r, c+1, 1)
            else:
                d = 1

        else: # 서
            if 0 <= r+1 < N and arr[r+1][c] == 0:
                return start_clean(r+1, c, 2)
            else:
                d = 2
    return

def around_4_available(i, j):
    check = False
    for z in range(4):
        ni = i + di[z]
        nj = j + dj[z]
        if 0 <= ni < N and 0 <= nj < M:
            if arr[ni][nj] == 0:
                check = True
                break

    return check

def start_clean(r, c, d):
    global ans
    if arr[r][c] == 0: # 만약 현재 위치한 칸이 청소하기 전의 빈 칸이라면
        ans += 1 # 청소한 칸 개수 1 증가시키고
    arr[r][c] = 2 # 청소했다는 표시를 세우지
    if around_4_available(r, c): # 청소를 다 한 후 주변 4개의 칸에 빈 칸이 있으면
        return find_clean_blank(r, c, d) # 주변의 4칸중 청소할 칸을 정해주는 함수를 실행시키자
    else:
        if d == 0:
            if 0 <= r + 1 < N and arr[r+1][c] == 2:
                return start_clean(r+1, c, d)
            else:
                return
        elif d == 1:
            if 0 <= c - 1 < M and arr[r][c-1] == 2:
                return start_clean(r, c-1, d)
            else:
                return
        elif d == 2:
            if 0 <= r - 1 < N and arr[r-1][c] == 2:
                return start_clean(r-1, c, d)
            else:
                return
        else:
            if 0 <= c + 1 < M and arr[r][c+1] == 2:
                return start_clean(r, c+1, d)
            else:
                return

N, M = map(int, input().split()) # 로봇 청소기가 돌아야 하는 방의 넓이
r, c, d = map(int, input().split()) # r, c는 로봇 청소기의 좌표, d는 로봇 청소기가 바라보고 있는 방향
arr = [] # 방의 정보가 저장될 리스트
for i in range(N):
    arr.append(list(map(int, input().split()))) # 1은 벽, 0은 청소 가능한 빈 칸

ans = 0 # 청소한 칸의 수
start_clean(r, c, d) # 청소 함수
print(ans)