import sys
sys.stdin = open('input_1238.txt')
from collections import deque

def bfs2(student):
    q = deque()
    visited = ['inf'] * (n + 1) # 방문기록, 해당 지점까지 도달하는데 걸린 시간을 업데이트
    q.append([x, 0]) # 학생의 번호와 지금까지 쌓인 이동거리
    while q:
        now_city, now_road = q.popleft()

        # 현재 도시에서 이동 가능한 도시 리스트업(visited 테이블 활용, 만약 지금 저장된 이동시간보다 
        # 더 짧은 시간으로 이동 가능하다면 갱신 후 큐에 넣기)
        for i in injeup_list[now_city]:
            # i의 값은 [마을, 이동시간]의 형태로 들어가있음
            next_city, to_next_road = i
            if visited[next_city] == 'inf' or visited[next_city] > to_next_road + now_road:
                visited[next_city] = to_next_road + now_road
                q.append([next_city, to_next_road + now_road])
    
    return visited[student]

def bfs(student):
    q = deque()
    visited = ['inf'] * (n + 1) # 방문기록, 해당 지점까지 도달하는데 걸린 시간을 업데이트
    q.append([student, 0]) # 학생의 번호와 지금까지 쌓인 이동거리
    while q:
        now_city, now_road = q.popleft()

        # 현재 도시에서 이동 가능한 도시 리스트업(visited 테이블 활용, 만약 지금 저장된 이동시간보다 
        # 더 짧은 시간으로 이동 가능하다면 갱신 후 큐에 넣기)
        for i in injeup_list[now_city]:
            # i의 값은 [마을, 이동시간]의 형태로 들어가있음
            next_city, to_next_road = i
            if visited[next_city] == 'inf' or visited[next_city] > to_next_road + now_road:
                visited[next_city] = to_next_road + now_road
                q.append([next_city, to_next_road + now_road])
    
    return visited[x]

# N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.
# 어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다.
# 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.
# 각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다.
# 하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.
# 이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다.
# N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

n, m, x = map(int, input().split())
# 인접리스트로 받자
injeup_list = [[] for _ in range(n + 1)]
for i in range(m):
    start, end, time = map(int, input().split())
    injeup_list[start].append([end, time])

# print(injeup_list)
# injeup_list[a] -> a번째 도시와 연결되어 있는 [마을, 이동시간]의 목록

# 학생별로 x에 왕복하는데 필요한 시간을 정리하자.
min_list = []
for i in range(1, n + 1):
    go_min = bfs(i)
    come_min = bfs2(i)
    min_list.append(go_min + come_min)

min_list[x] = 0
# print(min_list)
min_list.sort()
print(min_list[-1])