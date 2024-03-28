import sys
sys.stdin = open('input1865.txt')
from collections import deque
input = sys.stdin.readline

def find_ans(target): # 시작 지점. 1~n중 하나의 값
    q = deque()
    time = 0
    q.append([target, time]) # 시작 지점, 이동하는데 걸린 시간
    visited_road = [0] * (n + 1)
    visited_hole = [0] * (n + 1)
    while q:
        now_r, now_time = q.popleft() # 현재 지점, 현재까지 누적된 시간
        if now_r == target and now_time < 0:
            return 'YES'

        for i in range(n+1):
            if hole[now_r][i] != 0 and visited_hole[i] == 0:
                visited_hole[i] = 1
                q.append([i, now_time + hole[now_r][i]])

        for i in range(n+1):
            if road[now_r][i] != 0 and visited_road[i] == 0:
                visited_road[i] = 1
                q.append([i, now_time + road[now_r][i]])



# n개의 지점이 있고, n개의 지점 사이에는 m개의 도로와 w개의 웜홀이 있다.
# 도로는 방향이 없고, 웜홀은 방향이 있다.
# 웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데, 특이하게도 도착을 하게 되면 시작을 하였을때 보다 시간이 뒤로 가게 됨
# 한 지점에서 출발해서 시간여행 시작, 다시 출발했던 위치로 돌아왔을 때, 출발을 했을 때 보다 시간이 되돌아간 경우가 있는지 없는지 찾아내자

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    # n: 지점의 수, m: 도로의 개수, w: 웜홀의 개수
    road = [[0] * (n + 1) for __ in range(n + 1)]
    hole = [[0] * (n + 1) for ___ in range(n + 1)]

    for i in range(m):
        s, e, t = map(int, input().split())
        road[s][e] = t
        road[e][s] = t

    for i in range(w):
        s, e, t = map(int, input().split())
        hole[s][e] = t * (-1)
    flag = 0
    for i in range(1, n+1):
        if find_ans(i) == 'YES':
            print("YES")
            flag = 1
            break

    if flag:
        pass
    else:
        print("NO")