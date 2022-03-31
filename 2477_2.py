import sys
sys.stdin = open('2477.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
# 큰 리스트 만든 후 거기에 그려보자
check_list = [[0]*1005 for __ in range(1005)]

# arr를 순회하며, i[0]의 값에 따라 이동 방향을 다르게 설정해주자. 델타 탐색 ㄱ
x, y = 500, 500
start = check_list[x][y]
for i in arr:
    if i[0] == 1: # 동쪽
        for z in range(i[1]):
            check_list[x][y+z] = 1
        x = x
        y = y + i[1] - 1
    elif i[0] == 2: # 서쪽
        for zz in range(i[1]):
            check_list[x][y-zz] = 1
        x = x
        y = y - (i[1] - 1)
    elif i[0] == 3: # 남쪽
        for zzz in range(i[1]):
            check_list[x+zzz][y] = 1
        x = x + i[1] - 1
        y = y
    elif i[0] == 4: # 북쪽
        for zzzz in range(i[1]):
            check_list[x-zzzz][y] = 1
        x = x - (i[1] - 1)
        y = y

cnt = 0
for k in range(1005):
    for q in range(1005):
        if check_list[k][q] == 1:
            cnt += 1
ans = cnt*N
print(check_list)

# 이렇게 하면 테두리만 칠해진다. 안까지 칠해야 하는데, 쉽지 않다