import sys
sys.stdin = open('input_1260.txt')
from collections import deque

def dfs(start_node):
    visited[start_node] = 1
    print(start_node, end=' ')
    for i in range(1, n + 1):
        if link_state[start_node][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

def bfs(start_node):
    q = deque()
    q.append(start_node)
    visited = [0] * (n + 1)
    visited[start_node] = 1

    while q:
        now_node = q.popleft()
        print(now_node, end=' ')
        for i in range(1, n + 1):
            if link_state[now_node][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)


n, m, v = map(int, input().split())
link_state = [[0] * (n + 1) for _ in range(n + 1)] # 인덱스와 노드의 번호를 맞출 수 있음
for i in range(m):
    a, b = map(int, input().split())
    link_state[a][b] = 1
    link_state[b][a] = 1

visited = [0] * (n + 1)

# 첫줄: DFS 결과 출력
dfs(v)
print()
# 둘쨋줄: BFS 결과 출력
bfs(v)