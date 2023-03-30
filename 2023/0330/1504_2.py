import sys
import heapq
sys.stdin = open('input1504.txt')
input = sys.stdin.readline
from collections import deque

def dijkstra(start):
    queue = []
    heapq.heappush(queue, [0, start])
    distance = [10**9]*(N+1)
    distance[start] = 0
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distance[current_node] < current_distance:
            continue
        for adjacent in adj_list[current_node]:
            adjacent_distance, adjacent_node = adjacent
            new_distance = current_distance + adjacent_distance
            if new_distance < distance[adjacent_node]:
                distance[adjacent_node] = new_distance
                heapq.heappush(queue, [new_distance, adjacent_node])
    return distance

N, E = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(E)]
v1, v2 = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
for a, b, c in arr:
    adj_list[a].append([c, b])
    adj_list[b].append([c, a])

# 시작점, v1, v2, 도착점으로 총 4번의 다익스트라를 실행합니다.
start_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)
end_distance = dijkstra(N)

# 시작점->v1->v2->도착점, 시작점->v2->v1->도착점 중 최소 거리를 출력합니다.
answer1 = start_distance[v1] + v1_distance[v2] + end_distance[v2]
answer2 = start_distance[v2] + v2_distance[v1] + end_distance[v1]
result = min(answer1, answer2)

if result < 10**9:
    print(result)
else:
    print(-1)