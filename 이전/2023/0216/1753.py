import sys
from pprint import pprint
from collections import deque
sys.stdin = open('1753input.txt')

def di(K):
    queue = deque()
    visited[K] = 1
    ans_list[K] = 0
    for i in range(len(relation_arr[K])):
        ans_list[relation_arr[K][i][0]] = relation_arr[K][i][1]

    # pprint(ans_list)
    min_node = K
    min_node_length = 1000000000
    for i in range(1, len(ans_list)):
        if ans_list[i] < min_node_length:
            min_node_length = ans_list[i]
            min_node = i
    queue.append(min_node)
    # print(min_node)
    while queue: # 노드를 모두 방문하기 전 까지
        # K노드에서 가까이 있는 노드 위주로 진행. min_node에서 시작하는 순회
        # print(visited)
        min_node = queue.popleft()
        before_node = ans_list[min_node] # K 에서 min_node까지 이동하는 값
        visited[min_node] = 1

        for i in range(len(relation_arr[min_node])):
            if relation_arr[min_node][i][1] + before_node < ans_list[relation_arr[min_node][i][0]]:
                ans_list[relation_arr[min_node][i][0]] = relation_arr[min_node][i][1] + before_node

        min_node_length = 1000000000
        # print(ans_list)
        for i in range(1, len(ans_list)):
            if visited[i] == 0 and ans_list[i] < min_node_length:
                min_node_length = ans_list[i]
                min_node = i
        if min_node_length == 1000000000:
            pass
        else:
            queue.append(min_node)
        # print(min_node, min_node_length)


V, E = map(int, input().split()) # V: 정점의 개수, E: 간선의 개수
K = int(input()) # 시작점
arr = []
for i in range(E):
    arr.append(list(map(int, input().split()))) # u, v, w -> u에서 v로 가는 간선의 가중치는 w

# 방향그래프가 주어지면 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성
# 가중치를 이차원 리스트에 표현해보면 좋을 것 같다.
relation_arr = [[] for _ in range(V+1)] # 정점의 번호와 인덱스를 일치시켜주는 작업
# 인접 리스트를 이용해 메모리 단축
for i in range(len(arr)):
    relation_arr[arr[i][0]].append((arr[i][1], arr[i][2])) # relation_arr의 인덱스값이 출발점, 튜플의 첫 값이 도착점, 두번째 값이 가중치

# pprint(relation_arr)

ans_list = [10**9] * (V+1) # K에서 각 노드까지 걸리는 최단 거리를 저장할 예정
visited = [0] * (V+1)
di(K)
# 출력: i번째 줄에 시작점에서 i번째 간선으로의 최단거리를 출력. 자기 자신은 0, 경로 존재하지 않으면 INF 출력
for i in range(1, len(ans_list)):
    if ans_list[i] == 10**9:
        print('INF')
    else:
        print(ans_list[i])