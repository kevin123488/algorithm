# 출처 -> https://www.acmicpc.net/problem/1976
import sys
sys.stdin = open('input_1976.txt')
from collections import deque

def bfs():
    q = deque()
    now_idx = 0
    q.append(plan[now_idx])

    while q:
        now_city = q.popleft()
        if now_city == plan[now_idx]:
            if now_idx == len(plan) - 1:
                return 'YES'
            else:
                now_idx += 1

        for i in range(len(city_link[now_city - 1])):
            if city_link[now_city - 1][i] == 1:
                q.append(i + 1)
    
    return 'NO'

n = int(input())
m = int(input())
city_link = [list(map(int, input().split())) for _ in range(n)]
# city_link[a - 1][b - 1] == 1 -> a와 b는 연결되어있음. 0이면 연결 X
plan = list(map(int, input().split()))

print(bfs())