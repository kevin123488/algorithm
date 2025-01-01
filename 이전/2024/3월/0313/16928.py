import sys
from collections import deque
sys.stdin = open('16928.txt')

def bfs():
    q.append([1, 0]) # 시작칸은 1, 현재 횟수는 0
    board_visited[1] = 1
    while q:
        horse, cnt = q.popleft()
        if horse == 100:
            return cnt

        for i in range(1, 7): # 주사위 눈
            if horse + i in ladder_start and board_visited[horse + i] == 0: # 사다리 탈 수 있는 칸
                # 사다리 타고 해당 칸으로 이동
                next_ladder_horse = 0
                for j in ladder:
                    if j[0] == horse + i:
                        next_ladder_horse = j[1]
                q.append([next_ladder_horse, cnt + 1]) # 주사위 한 번으로 사다리 타고 난 후의 칸까지 이동 가능
                
                board_visited[horse + i] = 1
                board_visited[next_ladder_horse] = 1

            elif horse + i in snake_start and board_visited[horse + i] == 0: # 뱀 탈 수 있는 칸
                # 뱀 타고 해당 칸으로 이동
                next_snake_horse = 0
                for j in snake:
                    if j[0] == horse + i:
                        next_snake_horse = j[1]
                q.append([next_snake_horse, cnt + 1])
                
                board_visited[horse + i] = 1
                board_visited[next_snake_horse] = 1

            elif horse + i <= 100 and board_visited[horse + i] == 0:
                q.append([horse + i, cnt + 1])
                board_visited[horse + i] = 1
    


n, m = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(n)] # [x, y] x번 칸에 도착 -> y번 칸으로 이동, x < y
snake = [list(map(int, input().split())) for _ in range(m)] # [u, v] u번 칸에 도착 -> v번 칸으로 이동, u > v
ladder_start = []
ladder_fin = []
snake_start = []
snake_fin = []
for i in ladder:
    start = i[0]
    fin = i[1]
    ladder_start.append(start)
    ladder_fin.append(fin)

for i in snake:
    start = i[0]
    fin = i[1]
    snake_start.append(start)
    snake_fin.append(fin)

board = [i for i in range(101)]
board_visited = [0] * 101

# 주사위 사용, 주사위를 굴려 나온 수만큼 이동
# 현재 칸 + 주사위 눈 의 값에 해당하는 칸으로 이동
# 100 넘어간다면 이동 불가
# 도착한 칸이 사다리 -> 사다리 타고 위로 이동
# 도착한 칸이 뱀 -> 뱀 타고 아래로 이동
# 100번 칸에 도착하기 위해 최소로 굴려야 하는 횟수의 최솟값

# 각 칸의 숫자와 인덱스간의 관계
# i 인덱스 * 10 + j 인덱스 + 1 = 각 칸에 적혀있는 수
# 주사위 눈만큼 칸의 값이 증가한다고 생각하면 됨
# 뱀 타면 값이 적은 칸으로 이동, 사다리 타면 값이 높은 칸으로 이동

q = deque()
print(bfs())