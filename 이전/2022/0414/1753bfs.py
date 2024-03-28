import sys
sys.stdin = open('1753.txt')
input = sys.stdin.readline
from collections import deque

def bfs(a, b, cnt):
    global ans
    que = deque()
    que.append((a, b, cnt))
    while que:
        a, b, cnt = que.popleft()
        if a == b:
            if ans > cnt:
                ans = cnt
            continue

        if cnt > ans:
            continue

        for i in range(len(injeup[a])):
            if injeup[a][i] != 0 and visited[injeup[a][i][0]] == 0:
                que.append((injeup[a][i][0], b, cnt+injeup[a][i][1]))


V, E = map(int, input().split()) # V: 정점의 개수, E: 간선의 개수
s = int(input()) # s: 시작 정점
arr = [list(map(int, input().split())) for _ in range(E)] # (u에서, v까지, 가중치w)

# 서로 다른 두 정점 사이에 여러개의 간선이 존재할 수도 있음
# 첫 줄 부터 v개의 줄에 걸쳐 i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다
# 경로가 존재하지 않을 경우 INF 출력

visited = [0]*(V+1) # 인덱스와 정점의 번호를 맞춰주기 위해
# 인접 정보를 넣어줄 리스트를 만들 예정
injeup = [[0] for __ in range(V+1)]
for i in arr:
    injeup[i[0]].append([i[1], i[2]])
# print(injeup)
# [[0], [0, (2, 2), (3, 3)], [0, (3, 4), (4, 5)], [0, (4, 6)], [0], [0, (1, 1)]]

# bfs
for i in range(1, V+1):
    ans = 10000000
    bfs(s, i, 0) # 시작시의 가중치합은 0. 출발지점은 항상 s.
    if ans == 10000000:
        print('INF')
    else:
        print(ans)