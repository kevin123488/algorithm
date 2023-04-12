import sys
from collections import deque
sys.stdin = open('input1967.txt')
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

def dfs(start):
    visited = [False] * (n + 1)
    stack = deque()
    stack.append((start, 0))
    # stack = [(start, 0)]
    visited[start] = True
    max_dist = (0, 0) # (node, dist)

    while stack:
        node, dist = stack.pop()
        if dist > max_dist[1]:
            max_dist = (node, dist)
        for v, w in tree[node]:
            if not visited[v]:
                visited[v] = True
                stack.append((v, dist + w))

    return max_dist

node, _ = dfs(1)
node, dist = dfs(node)
print(dist)
