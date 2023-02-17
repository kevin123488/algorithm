import sys
from collections import deque
from pprint import pprint
sys.stdin = open('1753input.txt')

def di(K):
    queue.append(K)
    visited[K] = 1
    for i in range(len(relation_arr[K])):
        if relation_arr[i] != 0:  # 연결된 간선의 정보가 있을 때
            ans_list[i] = relation_arr[i]
    while True:
        pass

V, E = map(int, input().split()) # V: 정점의 개수, E: 간선의 개수
K = int(input()) # 시작점
arr = []
for i in range(E):
    arr.append(list(map(int, input().split()))) # u, v, w -> u에서 v로 가는 간선의 가중치는 w

# 방향그래프가 주어지면 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성
# 가중치를 이차원 리스트에 표현해보면 좋을 것 같다.
relation_arr = [[0] * (V+1) for _ in range(V+1)] # 정점의 번호와 인덱스를 일치시켜주는 작업
for i in arr:
    # 서로 다른 두 정점 사이에 2개 이상의 간선이 있을 수 있음
    if relation_arr[i[0]][i[1]] == 0: # 아직 추가되지 않았으면
        relation_arr[i[0]][i[1]] = i[2]
    elif relation_arr[i[0]][i[1]] > i[2]: # 기존의 값보다 적으면
        relation_arr[i[0]][i[1]] = i[2]

pprint(relation_arr)

ans_list = [10**9] * (V+1) # K에서 각 노드까지 걸리는 최단 거리를 저장할 예정
visited = [0] * (V+1)
queue = deque()
di(K)
# 출력: i번째 줄에 시작점에서 i번째 간선으로의 최단거리를 출력. 자기 자신은 0, 경로 존재하지 않으면 INF 출력