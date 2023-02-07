import sys
sys.stdin = open('11725.txt')
sys.setrecursionlimit(10**6)
def dfs(a): # 순회중인 노드의 번호를 입력받음
    for i in range(len(injeup[a])):
        if visited[injeup[a][i]] == 0:
            visited[injeup[a][i]] = a
            dfs(injeup[a][i])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N-1)]

# 위의 정보를 바탕으로 인접리스트를 만들어보자
# 조회중인 노드의 번호에 해당하는 위치에 해당 노드와 연결되어있는 노드들의 번호를 넣어주면?
injeup = [[] for _ in range(N+1)] # N+1개 만큼의 공간을 만들어, 노드 1부터 N까지를 번호와 인덱스가 일치하도록 하였다
for i in arr: # arr 순회하면서
    injeup[i[0]].append(i[1])
    injeup[i[1]].append(i[0]) # 인접 리스트에 정보를 넣어줌
visited = [0]*(N+1) # 노드의 번호와 인덱스를 맞춰주기 위함

dfs(1) # 루트가 되는 노드는 1 이므로, 1부터 시작하면 됨
for i in range(2, len(visited)):
    print(visited[i])