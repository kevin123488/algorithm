import sys
sys.stdin = open('14499.txt')

# 주사위 모든 면에 0이 적혀있음
# 굴려가며 주사위의 수를 바꿔감. 처음 놓인 좌표의 값(지도)은 항상 0에서 시작됨
# 지도의 값이 0이면 지도-주사위 맞닿은 면의 값이 지도에 복사되고, 지도의 값이 0이 아닐 경우 지도의 값이 맞닿은 주사위의 바닥면에 복사된 후 지도의 값은 0이 된다.
# 시작할 때 주사위 모든 면의 값은 0

def to_one(a, b):
    # 동쪽으로 이동(굴림)
    # 주사위 전개도 기준 각 면의 값이 어떻게 바뀌는지부터 확인이 필요
    if map_list[a][b] == 0:
        map_list[a][b] = dice[3]
    else:
        dice[3] = map_list[a][b]
        map_list[a][b] = 0
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[0], dice[2], dice[3], dice[5], dice[4], dice[1]
    print(dice[5])


def to_two(a, b):
    # 서쪽으로 이동(굴림)
    if map_list[a][b] == 0:
        map_list[a][b] = dice[1]
    else:
        dice[1] = map_list[a][b]
        map_list[a][b] = 0
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[0], dice[5], dice[1], dice[2], dice[4], dice[3]
    print(dice[5])


def to_three(a, b):
    # 북쪽으로 이동(굴림)
    if map_list[a][b] == 0:
        map_list[a][b] = dice[0]
    else:
        dice[0] = map_list[a][b]
        map_list[a][b] = 0
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[3], dice[2], dice[4]
    print(dice[5])


def to_four(a, b):
    # 남쪽으로 이동(굴림)
    if map_list[a][b] == 0:
        map_list[a][b] = dice[4]
    else:
        dice[4] = map_list[a][b]
        map_list[a][b] = 0
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[4], dice[3], dice[5], dice[0]
    print(dice[5])


n, m, x, y, k = map(int, input().split()) # n, m은 지도의 크기, x, y는 주사위를 놓은 곳의 좌표, k는 명령의 개수
map_list = []
for i in range(n):
    map_list.append(list(map(int, input().split())))

order_list = list(map(int, input().split())) # 1: 동쪽, 2: 서쪽, 3: 북쪽, 4: 남쪽

# 단순하게 생각하면 주사위 6면과 동서남북 조합해서 24가지 함수 만들면 되긴 함
# 근데 이게 맞나? 너무 막 짜는것 아닌가 싶음. 함수 선언과 조회가 많으면 스택이 쌓여 메모리 초과가 날 수 있음. 주의

# 초기 주사위의 모양은 다음과 같음
#     0
#    123
#     4
#     5
# 좌상 -> 우하 순으로 이동한다고 하자. 편의상 0 ~ 5의 순서 부여. (idx)
dice = [0, 0, 0, 0, 0, 0]

# 동쪽
#     0
#    235
#     4
#     1

# 서쪽
#     0
#    512
#     4
#     3

# 북쪽
#     5
#    103
#     2
#     4

# 남쪽
#     2
#    143
#     5
#     0

di = [0, 0, -1, 1] # 동, 서, 북, 남
dj = [1, -1, 0, 0]
now_i = x
now_j = y
for i in order_list:
    next_i = now_i + di[i - 1]
    next_j = now_j + dj[i - 1]
    if 0 <= next_i < n and 0 <= next_j < m:
        if i == 1:
            to_one(next_i, next_j)
        elif i == 2:
            to_two(next_i, next_j)
        elif i == 3:
            to_three(next_i, next_j)
        else:
            to_four(next_i, next_j)
        now_i = next_i
        now_j = next_j

# 첫 전개도: 0, 1, 2, 3, 4, 5
# 동쪽으로 이동한 후 펼친 전개도: 0, 2, 3, 5, 4, 1
# 남쪽으로 이동한 후 펼친 전개도: 2, 1, 4, 3, 5, 0
# 예시: 0, 0, 0, 0, 3, 0
# 동쪽으로 이동한 후: 0, 0, 0, 0, 3, 0
# 남쪽으로 이동한 후: 0, 0, 3, 0, 0, 0