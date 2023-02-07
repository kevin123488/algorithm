# baek 2580 스도쿠 문제
# 가로, 세로, 3*3 정사각형 9개에 각각 1~9까지의 숫자가 하나씩 들어가 있어야됨

import sys
sys.stdin = open('2580.txt')

def isitok(arr): # arr(9개의 숫자)를 입력받으면 스도쿠의 규칙을 만족하는지 아닌지 판별해줌
    if len(set(arr)) == 9: # 서로 다른 숫자 9개(0이 아닌)로 구성되어 있다면? -> 만족
        return 1 # 스도쿠 만족
    else:
        return 0

def dfs(a, b): # 채워줘야 하는 칸의 좌표 인덱스를 받아오자
    visited = []
    for i in range(9):
        visited += [arr[i][b]]
        visited += [arr[a][i]]
    # 위의 과정을 통해 0인 좌표의 i행과 j열의 숫자들이 visited에 들어가게 됨
    # 정사각형 범위의 값을 넣어주자
    if 0<=a<=2 and 0<=b<=2:
        for z in range(3):
            for x in range(3):
                visited += [arr[z][x]]
    if 3<=a<=5 and 0<=b<=2:
        for z in range(3, 6):
            for x in range(3):
                visited += [arr[z][x]]
    if 6<=a<=8 and 0<=b<=2:
        for z in range(6, 9):
            for x in range(3):
                visited += [arr[z][x]]
    if 0<=a<=2 and 3<=b<=5:
        for z in range(3):
            for x in range(3, 6):
                visited += [arr[z][x]]
    if 3<=a<=5 and 3<=b<=5:
        for z in range(3, 6):
            for x in range(3, 6):
                visited += [arr[z][x]]
    if 6<=a<=8 and 3<=b<=5:
        for z in range(6, 9):
            for x in range(3, 6):
                visited += [arr[z][x]]
    if 0<=a<=2 and 6<=b<=8:
        for z in range(3):
            for x in range(6, 9):
                visited += [arr[z][x]]
    if 3<=a<=5 and 6<=b<=8:
        for z in range(3, 6):
            for x in range(6, 9):
                visited += [arr[z][x]]
    if 6<=a<=8 and 6<=b<=8:
        for z in range(6, 9):
            for x in range(6, 9):
                visited += [arr[z][x]]

    for ii in range(1, 10):
        if ii not in set(visited):
            arr[a][b] = ii
            dfs()


arr = [list(map(int, input().split())) for _ in range(9)] # 9*9의 배열을 받음

# 빈 칸은 0으로 표현
# 판별하는 방법을 찾아보자. 가로, 세로, 정사각형 내의 숫자들의 분포를 체크해야 한다

# 0 칸에 값을 입력해주는 방법을 찾아보자
# 어떤 방법을 택할 것인가?
# 1. 0인 칸을 발견한다
# 2. 해당 칸이 속한 가로줄, 세로줄, 3*3 정사각형 내의 숫자들을 받아온다
# 3. 거기 없는 숫자중 아무거나 (되도록 적은 수 부터)넣어준다
# 4. 위의 연산을 반복. 만약 조건을 만족하는 숫자가 없을 경우 return
# 5. 그렇게 해서 arr의 모든 0을 적절한 값으로 바꾸어 줬다면?
# 6. 해당 arr를 출력하자
flag = 0
for i in range(9):
    if flag == 1:
        break
    for j in range(9):
        if arr[i][j] == 0: # 채워줘야 하는 칸이면
            print(set(dfs(i, j)))
            flag += 1
            break