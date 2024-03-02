import sys
from collections import deque
sys.stdin = open('1005.txt')

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    build_time = list(map(int, input().split()))
    build_seq = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    dp = [0] * (n + 1)

    for i in range(k):
        x, y = map(int, input().split())
        build_seq[x].append(y)
        in_degree[y] += 1

    w = int(input())
    q = deque()

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
            dp[i] = build_time[i - 1]
    
    while q:
        v = q.popleft()
        for i in build_seq[v]:
            in_degree[i] -= 1
            dp[i] = max(dp[i], dp[v] + build_time[i - 1])
            if in_degree[i] == 0:
                q.append(i)

    print(dp[w])