# 동혁이는 친구들과 함께 여행을 가려고 한다. 한국에는 도시가 N개 있고 임의의 두 도시 사이에 길이 있을 수도,
# 없을 수도 있다. 동혁이의 여행 일정이 주어졌을 때, 이 여행 경로가 가능한 것인지 알아보자.
# 물론 중간에 다른 도시를 경유해서 여행을 할 수도 있다. 예를 들어 도시가 5개 있고, A-B, B-C, A-D, B-D, E-A의 길이 있고,
# 동혁이의 여행 계획이 E C B C D 라면 E-A-B-C-B-C-B-D라는 여행경로를 통해 목적을 달성할 수 있다.
# 도시들의 개수와 도시들 간의 연결 여부가 주어져 있고, 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때
# 가능한지 여부를 판별하는 프로그램을 작성하시오. 같은 도시를 여러 번 방문하는 것도 가능하다.

import sys
sys.stdin = open('input_1976.txt')
from collections import deque

def bfs(start, end, visited, n):
    q = deque()
    q.append(start)
    while q:
        now_city = q.popleft()
        visited[now_city] = 1
        if now_city == end:
            return True
        
        for i in range(1, n + 1):
            if linked_list[now_city][i] == 1 and visited[i] == 0:
                q.append(i)
    
    return False

n = int(input())
m = int(input())
linked_list = [[0] * (n + 1)]
for i in range(n):
    temp_list = list(map(int, input().split()))
    temp_list = [0] + temp_list
    linked_list.append(temp_list)

journey = list(map(int, input().split()))
# 여행 경로대로 이동 가능한지 판별

flag = 0
for i in range(m - 1):
    start = journey[i]
    end = journey[i + 1]
    visited = [0] * (n + 1)
    journey_tf = bfs(start, end, visited, n)
    if journey_tf == False:
        print('NO')
        flag = 1
        break
    else:
        continue

if flag == 0:
    print('YES')