# dfs로 풀어보자
import sys
sys.stdin = open('1753.txt')

def dfs(a, b, cnt):
    global ans
    visited[a] = 1

    if cnt > ans:
        return
    if a == b:
        if ans > cnt:
            ans = cnt
        return

    for i in range(len(arr)): # 조회중인 정점과 연결되어있는 애들을 찾아보자
        if arr[i][0] == a and visited[arr[i][1]]: # 정점이 연결되어 있으면서 방문하지 않은 곳 이라면
            dfs(arr[i][1], b, cnt+arr[i][2])
            visited[arr[i][1]] = 0

V, E = map(int, input().split()) # V: 정점의 개수, E: 간선의 개수
s = int(input()) # 시작 정점의 번호. (정점은 1부터 시작)
arr = [list(map(int, input().split())) for _ in range(E)] # u, v, w의 정보가 들어있음
# u에서 v로 가는 가중치 w인 간선이 존재한다는 의미
# 서로 다른 두 정점 사이에 여러개의 간선이 존재할 수도 있다
# visited = [1] + [0]*V # 인덱스와 정점의 번호를 맞춰주기 위함
# 출력은? 첫 줄부터 V개의 줄에 걸쳐 i번째 줄에 i번 정점으로의 최단 경로의 값을 출력
# 인접행렬을 만들자
# injeup = [[0]*(V+1) for _ in range(V+1)]
# for i in arr:
#     injeup[i[0]][i[1]] = [1, i[2]] # 해당 자리에 (연결여부, 가중치)를 넣어준다

for i in range(1, V+1):
    visited = [1] + [0]*V
    ans = 100000000
    dfs(s, i, 0) # s점에서 시작해 i점에 도달하는 경로중 가중치가 최소가 될 때의 값
    if ans < 100000000:
        print(ans)
    else:
        print('INF')