import sys
sys.stdin = open('input1504.txt')
input = sys.stdin.readline
from collections import deque

# 다익스트라 로직
# 1번에서 3번 노드로 간다 치면
# 1번과 연결되어있는 노드 순회(가중치 낮은 순으로)
# 1 -> 2 -> 2번과 연결되어 있는 노드 순회(가중치 낮은 순으로)
#

def bfs(start, end):
    # 다익스트라 구현
    # start점과 연결된 지점의 가중치를 gan_list에 입력
    gan_list = [10 ** 10] * (N + 1)
    visited = [0] * (N + 1)
    gan_list[0] = 0
    gan_list[start] = 0
    visited[start] = 1
    q = deque()
    # for i in range(len(inj_list[start])):
    #     gan_list[inj_list[start][i][1]] = inj_list[start][i][0]
    #     q.append(inj_list[start][i][1])
    q.append(start)
    while q:
        s = q.popleft()
        visited[s] = 1

        # s와 연결돼있는 정점들의 정보를 모아둔 리스트
        s_link = inj_list[s]
        for i in range(len(s_link)):
            if gan_list[s_link[i][1]] > gan_list[s] + s_link[i][0]:
                gan_list[s_link[i][1]] = gan_list[s] + s_link[i][0]

        # s와 연결된 노드 중 가장 가중치가 낮은 노드를 선택, 해당 노드에서 다시 탐색
        for i in range(len(s_link)):
            if visited[s_link[i][1]] == 0:
                q.append(s_link[i][1])
    return gan_list[end]

def find_di():
    ans1 = bfs(1, v1)
    ans2 = bfs(v1, v2)
    ans3 = bfs(v2, N)
    return_1 = ans1 + ans2 + ans3
    ans4 = bfs(1, v2)
    if ans4 > return_1:
        return return_1
    ans5 = bfs(v2, v1)
    if ans4 + ans5 > return_1:
        return return_1
    ans6 = bfs(v1, N)
    return_2 = ans4 + ans5 + ans6
    return min(return_1, return_2)

# 방향성 없는 그래프 주어짐
# 1번 정점에서 N번 정점으로 최단거리 이동
# 임의로 주어진 두 정점은 반드시 통과
# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있음. 하지만 반드시 최단 경로로 이동해야 함
# 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램 작성

N, E = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(E)]
v1, v2 = map(int, input().split())

# 인접리스트
# 인덱스가 해당 노드, []안에 들어있는 값이 해당 인덱스의 노드와 연결되어 있는 노드의 정보
inj_list = [[] for _ in range(N + 1)]
for i in arr:
    inj_list[i[0]].append([i[2], i[1]])
    inj_list[i[1]].append([i[2], i[0]])

for i in inj_list:
    i.sort()
# [[], [[3, 2], [5, 3], [4, 4]], [[3, 1], [3, 3], [5, 4]], [[3, 2], [1, 4], [5, 1]], [[1, 3], [5, 2], [4, 1]]]
# [[], [[3, 2], [4, 4], [5, 3]], [[3, 1], [3, 3], [5, 4]], [[1, 4], [3, 2], [5, 1]], [[1, 3], [4, 1], [5, 2]]] -> 정렬 후
# 1번째 노드와 2, 3, 4가 연결되어 있으며, 그 거리는 각각 3, 5, 4이다. 위의 인접 리스트는 가중치(0번째 값)가 낮은 순으로 노드의 번호(1번째 값)이 들어가 있다.
# 가중치가 있을 때의 최단거리 -> 다익스트라 사용
# 로직
# 시작점
# 시작점과 연결되어 있는 간선 중 가중치가 가장 낮은 간선에 연결되어 있는 노드 탐색
# 해당 노드에서 가장

# 1번에서 해당 노드까지 가기 위해 필요한 거리
gan_list = [10**10] * (N + 1)
visited = [0] * (N + 1)
gan_list[0] = 0
# 1에서 v1, v1에서 v2로 갈 때의 최단거리와
# 1에서 v2, v2에서 v1으로 갈 때의 최단거리를 모두 구한 후
# 비고해 더욱 짧은 거리를 출력
print(find_di())