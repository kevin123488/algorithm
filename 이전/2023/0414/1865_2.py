from collections import deque

# BFS 함수 정의
def bfs(start):
    # 시작점 큐에 삽입하고 방문 체크
    queue = deque([start])
    visited[start] = True

    # BFS 탐색
    while queue:
        curr = queue.popleft()
        # 인접한 노드 탐색
        for neighbor, weight in graph[curr]:
            # 현재 노드에서 인접한 노드로 이동하는데 걸리는 시간 계산
            next_time = distances[curr] + weight
            # 만약 현재 노드에서 인접한 노드로 이동하는데 걸리는 시간이 더 작은 경우
            if next_time < distances[neighbor]:
                # 거리 갱신
                distances[neighbor] = next_time
                # 큐에 삽입하고 방문 체크
                queue.append(neighbor)
                visited[neighbor] = True
                # 만약 출발 노드에서 다시 출발 노드로 돌아온 경우
                if neighbor == start:
                    # 시간이 줄어들기 때문에 가능한 경우
                    return True
    # BFS 탐색 후에도 출발 노드에서 도달할 수 없는 경우 불가능한 경우
    return False

# 테스트 케이스 개수 입력
t = int(input())

# 테스트 케이스 반복문
for _ in range(t):
    # 지점 수, 도로 수, 웜홀 수 입력
    n, m, w = map(int, input().split())

    # 그래프 초기화
    graph = [[] for _ in range(n+1)]

    # 도로 정보 입력
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    # 웜홀 정보 입력
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

    # 출발 노드별로 최단 거리 계산
    possible = False
    for start in range(1, n+1):
        # 초기화
        distances = [float('inf')] * (n+1)
        visited = [False] * (n+1)
        # 출발 노드의 최단 거리는 0
        distances[start] = 0

        # 출발 노드에서 시작하는 BFS 탐색
        if bfs(start):
            possible = True
            break

    # 가능한 경우 "YES", 불가능한 경우 "NO" 출력
    print("YES" if possible else "NO")