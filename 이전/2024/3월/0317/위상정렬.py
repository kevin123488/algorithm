from collections import deque

# 위상정렬 알고리즘
def topo_sort():
    ans_list = [] # 순서를 반환할 리스트 생성

    while q:
        now_node = q.popleft() # 큐에서 순차적으로 노드를 빼냄
        ans_list.append(now_node) # 빼낸 노드는 순서 반환 리스트에 넣음

        for i in node_relation[now_node]: # 방문한 노드를 기준으로 '해당 노드 방문시 방문이 가능해지는 노드'를 확인
            # i는 after_node들
            in_degree[i] -= 1 # 선수노드를 방문하였으므로 진입차수 감소
            if in_degree[i] == 0: # 진입차수가 0 -> 선수노드를 모두 방문함
                q.append(i) # 순서 반환 리스트에 추가

    return ans_list


n = int(input()) # 방문예정인 노드의 수를 입력받자
k = int(input()) # 노드간의 선수 정보를 입력받을 횟수
node_rel = [list(map(int, input().split())) for _ in range(k)] # 노드간의 선수 정보 입력
node_relation = [[] for _ in range(n + 1)] # 노드간의 선수 정보 저장
in_degree = [0] * (n + 1) # 진입차수 저장할 리스트

for i in range(k):
    before_node, after_node = node_rel[i]
    # before_node: 선수가 되는 노드, after_node: 선수노드를 방문해야 방문 가능한 노드
    node_relation[before_node].append(after_node) # 인덱스 값에 해당하는 노드를 선수노드로 갖는 값이 들어가도록 해야 함
    in_degree[after_node] += 1 # 진입차수 수정해주자. 진입차수란 해당 노드에 방문하기 위해 사전에 방문해야하는 노드의 수

q = deque() # 위상정렬 알고리즘을 위한 큐 생성

# 진입차수가 0인 노드를 시작점으로 넣어줌
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)

ans = topo_sort()