import sys
sys.stdin = open('1516.txt')
from collections import deque

def topo_sort():

    while q:
        now_node = q.popleft()
        for i in topo_building[now_node]: # 현재 노드를 선수로 갖는 노드
            in_degree[i] -= 1
            dp[i] = max(dp[i], dp[now_node] + building_time[i])
            if in_degree[i] == 0:
                q.append(i)

    return

n = int(input())
building_time = [0] * (n + 1)
topo_building = [[] for _ in range(1 + n)]
in_degree = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    node_topo_list = list(map(int, input().split()))
    build_time = node_topo_list[0]
    building_time[i] = build_time

    for j in range(1, len(node_topo_list) - 1):
        topo_building[node_topo_list[j]].append(i)
        in_degree[i] += 1

q = deque()

for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)
        dp[i] = building_time[i]

topo_sort()

for i in range(1, n + 1):
    print(dp[i])