import sys
sys.stdin = open('1260.txt')
from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, n + 1):
        if injeup_list[v][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited = [0] * (n + 1)
    visited[v] = 1
    while q:
        now_node = q.popleft()
        print(now_node, end=' ')
        for i in range(1, n + 1):
            if injeup_list[now_node][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)


n, m, v = map(int, input().split())
injeup_list = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    # 정점은 1 ~ n 까지, injeup_list의 인덱스는 0 ~ n 까지
    node_a, node_b = map(int, input().split())
    injeup_list[node_a][node_b] = 1
    injeup_list[node_b][node_a] = 1

visited = [0] * (n + 1)
dfs(v)
print()
bfs(v)