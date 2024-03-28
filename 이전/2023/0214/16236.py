import sys
sys.stdin = open('16236input.txt')
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def shark_to_fish(i, j, k, l, shark): # 아기상어가 물고기를 잡기 위해 지나야 하는 칸의 최소 개수
    global visited
    # 최단거리로 이동하는 로직 필요
    # 이동 가능 여부도 판단해야 함
    visited[k][l] = 1
    queue = deque()
    length = 0
    queue.append([k, l, length])
    flag = 0
    while queue:
        start = queue.popleft()
        if start[0] == i and start[1] == j:
            flag = 1
            length = start[2]
            break
        for z in range(4):
            ni = start[0] + di[z]
            nj = start[1] + dj[z]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ni][nj] <= shark:
                    queue.append([ni, nj, start[2] + 1])
                    visited[ni][nj] = 1

    visited = [[0] * N for _ in range(N)]
    if flag == 1:
        return length
    else:
        return False

def find_can_eat(shark, k, l): # k, l 아기상어의 위치
    # 아기상어가 먹을 수 있는 물고기가 있는지 없는지 판별하는 함수
    ans = 6000
    where_to_go = []
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] < shark:
                length = shark_to_fish(i, j, k, l, shark)
                if length:
                    if ans > length:
                        ans = length
                        where_to_go = [[i, j]]
                    elif ans == length:
                        where_to_go.append([i, j])
    # 먹을 수 있는 물고기중 최단거리인 물고기가 2개 이상일 가능성이 있음
    # print(where_to_go)
    if len(where_to_go) >= 2:
        # 가장 위쪽에 있는 물고기를 고르는 로직
        eat_fish = []
        for i in where_to_go:
            if eat_fish == []:
                eat_fish = [i]
            elif eat_fish[0][0] > i[0]: # ex) eat_fish -> [[3, 1]], i -> [2, 1]
                eat_fish = [i]
            elif eat_fish[0][0] == i[0]:
                if eat_fish[0][1] > i[1]:
                    eat_fish = [i]

        where_to_go = eat_fish

    # if len(where_to_go) >= 2:
    #     eat_fish = []
    #     for i in where_to_go:
    #         if eat_fish == []:
    #             eat_fish = [i]
    #         elif eat_fish[0][1] > i[1]:
    #             eat_fish = [i]
    #         elif eat_fish[0][1] == i[1]:
    #             eat_fish.append(i)
    #
    #     where_to_go = eat_fish

    if ans == 6000:
        return False
    else:
        # print(ans, where_to_go)
        ans_list = [ans, where_to_go]
        return ans_list
    # 먹을 수 있는 물고기가 있다면, 이동 거리와 어느 좌표로 가야하는지 알려줌

def bfs(i, j, shark, ans):
    arr[i][j] = 0
    queue = deque()
    queue.append([i, j])
    shark_cnt = shark
    while queue:
        start = queue.popleft()
        ans_list = find_can_eat(shark, start[0], start[1])
        if ans_list:
            ans += ans_list[0]
            arr[ans_list[1][0][0]][ans_list[1][0][1]] = 0
            queue.append([ans_list[1][0][0], ans_list[1][0][1]])
            shark_cnt -= 1
            if shark_cnt == 0:
                shark += 1
                shark_cnt = shark
        else:
            break

    return ans

N = int(input()) # N*N 크기의 공간, 물고기 M 마리, 아기 상어 1마리
# 한 칸에는 물고기가 최대 1마리
# 아기 상어와 물고기는 모두 크기를 가지고 있음. 자연수
# 아기 상어의 초기 크기는 2, 1초에 상하좌우로 인접한 한 칸씩 이동
# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없음
# 나머지 칸은 모두 지나갈 수 있음
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있음. -> 크기가 동일한 경우 잡아먹지는 못하고 지나갈수만 있음
# 이동 로직
# 더 먹을 수 있는 물고기가 공간에 없다 -> 엄마 상어에게 도움
# 먹을 수 있는 물고기 1마리 -> 그 물고기 먹으러 감
# 먹을 수 있는 물고기가 1마리 이상 -> 가장 가까운 물고기 먹으러 감
# 거리: 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야 하는 칸의 ㄱ수의 최솟값
# 거리가 가까운 물고기가 많다면 가장 위에 있는 물고기를, 그런 물고기가 여러마리라면 가장 왼쪽의 물고기를 먹는다.

# 아기상어의 이동은 1초가 걸림, 물고기를 먹는데 걸리는 시간은 0초.
# 물고기를 먹으면 해당 칸은 빈 칸이 된다.
# 아기 상어는 자신의 크기와 '같은 수'의 물고기를 먹을 때마다 크기가 1 증가함
# 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있을까?

arr = []
shark = []
for i in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for j in range(len(temp)):
        if temp[j] == 9:
            shark = [i, j]

# print(arr)
# print(shark)
# 0: 빈 칸, 1~6: 칸에 있는 물고기의 크기, 9: 아기 상어
visited = [[0] * N for _ in range(N)]
ans = bfs(shark[0], shark[1], 2, 0)

print(ans)