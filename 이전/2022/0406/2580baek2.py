import sys
sys.stdin = open('2580.txt')

def rec(x, y, i):
    for k in range(3):
        for j in range(3):
            if i == arr[x//3*3+k][y//3*3+j]:
                return 0
    return 1

def col(x, i):
    for k in range(9):
        if i == arr[x][k]:
            return 0
    return 1

def row(y, i):
    for k in range(9):
        if i == arr[k][y]:
            return 0
    return 1

def dfs(a): # 조회중인 행
    if a == len(find_list):
        for i in range(9):
            print(*arr[i])
        exit(0) # 강제 종료 코드 # 이걸 이제 알다니

    # find_list에 받아둔 빈 칸 정보들을 이용하자
    x = find_list[a][0] # 빈 칸의 행 인덱스
    y = find_list[a][1] # 빈 칸의 열 인덱스
    for i in range(1, 10): # 빈 칸에 넣어줄 값, 1부터 9까지의 수가 들어갈 수 있음
        if col(x, i) and row(y, i) and rec(x, y, i):
            arr[x][y] = i # 다 만족하면 그때의 값을 넣어주자
            dfs(a+1) # 다음 빈칸으로 이동하고
            arr[x][y] = 0 # 다시 돌아와서 다른 경우도 찾아봐야 하기에 0으로 초기화 해주자
            
        

# 0인 칸에 숫자를 하나씩 대입해보자
arr = [list(map(int, input().split())) for _ in range(9)]
find_list = [] # 값을 넣어줘야 하는 빈칸이 담겨있는 리스트

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0: # 비었으면
            find_list.append((i, j))

dfs(0) # 0번째 행부터 조회를 시작할 예정