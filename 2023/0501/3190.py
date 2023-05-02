import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input3190.txt')
input = sys.stdin.readline

# 이동 방향
di = [-1, 1, 0, 0] # 상하좌우
dj = [0, 0, -1, 1] # 상하좌우

def play():
    direction = 3 # 오른쪽을 의미하는 인덱스
    start = [0, 0]
    apple[0][0] = 2
    tail = deque()
    tail.append(start)
    l = int(input())
    time = 0
    before_time = 0
    for i in range(l):
        ride = input().split()
        how_long = int(ride[0])
        where = ride[1]

        for k in range(how_long - before_time): # 이동 횟수
            ni = start[0] + di[direction]
            nj = start[1] + dj[direction]
            # 게임이 종료되지 않는 경우
            if 0 <= ni < n and 0 <= nj < n and apple[ni][nj] != 2: # apple_copy의 값이 2 -> 뱀의 몸통이 남아있는 경우
                time += 1
                start = [ni, nj]
                tail.append(start)
                if apple[ni][nj] == 0:
                    fin_tail = tail.popleft()
                    apple[fin_tail[0]][fin_tail[1]] = 0

                apple[ni][nj] = 2

            # 게임이 종료되는 경우
            else:
                return time + 1

        # 시간 다 지나면 방향 바꿔주기
        if where == 'L': # 현재 방향에서 왼쪽으로
            if direction == 0:
                direction = 2
            elif direction == 1:
                direction = 3
            elif direction == 2:
                direction = 1
            else:
                direction = 0
        else: # 현재 방향에서 오른쪽으로
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 0
            else:
                direction = 1

        before_time = how_long

    # 입력된 시간을 모두 소비하였을 경우, 그 때의 진행 방향으로 벽에 닿을 때까지 시간 추가해가며 탐색
    while True:
        ni = start[0] + di[direction]
        nj = start[1] + dj[direction]
        if 0 <= ni < n and 0 <= nj < n and apple[ni][nj] != 2:
            start = [ni, nj]
            time += 1
        else:
            return time + 1

n = int(input())
k = int(input())
apple = [[0] * n for _ in range(n)]
for i in range(k):
    height, width = map(int, input().split())
    apple[height-1][width-1] = 1

# 뱀은 사과를 먹으면 길이가 늘어난다.
# 뱀이 기어다니다 벽 또는 자기 자신과 몸이 부딪히면 게임이 끝난다.
# 뱀은 0, 0에서 출발하며, 해당 좌표엔 사과가 없다.
# 뱀의 시작 길이는 1
# 처음엔 오른쪽을 향한다.
# 뱀의 이동 방향은 L과 D가 있다. 각각 진행 방향의 왼쪽과 오른쪽으로 90도 회전시킨다는 뜻이다.
# 첫 입력이 D일 경우, 오른쪽을 바라보고 있는 뱀이 오른쪽으로 90도 꺾는다는 의미이므로 아래를 향하게 된다.
# 뱀의 이동 규칙
# 뱀은 먼저 몸의 길이를 늘린 후, 머리를 다음 칸에 위치시킨다.
# 이동한 칸에 사과가 있다? 그 칸에 있던 사과가 없어지고, 꼬리는 움직이지 않는다.
# 이동한 칸에 사과가 없다면? 몸길이를 줄여 꼬리가 위치한 칸을 비워준다. -> 몸길이는 변하지 않음
# 뱀은 매 초마다 이동하며, 방향을 꺾는 타이밍과 그 방향에 대한 정보가 주어진다.
# 뱀이 자기 자신의 꼬리에 부딪히거(나, 벽에 부딪힐 경우 게임은 종료된다.
# 몇 초에 게임이 끝나는지 구하자
print(play())