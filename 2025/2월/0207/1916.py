import sys
sys.stdin = open('input_1916.txt')
input = sys.stdin.readline
from pprint import pprint
import heapq

INF = 100000000

def djk(start_city):
    return_list = [INF for _ in range(n + 1)]
    return_list[start_city] = 0 # 자기 위치로는 이동 불가이므로
    pq = [] # 우선순위 큐
    heapq.heappush(pq, (0, start_city))

    while pq:
        now_cost, now_node = heapq.heappop(pq)
        if now_cost > return_list[now_node]:
            continue

        for i in linked_city[now_node]:
            next_node, next_cost = i
            if return_list[now_node] + next_cost < return_list[next_node]:
                heapq.heappush(pq, (return_list[now_node] + next_cost, next_node))
                return_list[next_node] = return_list[now_node] + next_cost
    
    return return_list

n = int(input())
m = int(input())

# 도시가 어떻게 연결되어있는지 체크
linked_city = [[] for _ in range(n + 1)]
# linked_city[n] -> 도시 n과 연결되어있는 도시의 정보
# [연결된 도시, 가중치] 의 형태로 정보가 들어가있음.
for i in range(m):
    start, arrive, cost = map(int, input().split())
    linked_city[start].append([arrive, cost])
    # linked_city[arrive].append([start, cost])

start_city, arrive_city = map(int, input().split())
djk_list = djk(start_city)
print(djk_list[arrive_city])