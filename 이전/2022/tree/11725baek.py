# tree 문제
import sys
sys.stdin = open('11725.txt')

def dfs(a): # 돌고 있는 노드의 번호를 넣어줌
    for i in range(len(injeup[a])):
        if injeup[a][i] == 1 and parent[i] == 0:
            parent[i] = a
            dfs(i)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N-1)]

# 인접행렬
# 무방향? 유방향?

injeup = [[0]*(N+1) for _ in range(N+1)] # 노드의 번호와 인덱스를 일치시켜 주기 위함
for i in arr:
    injeup[i[0]][i[1]] = 1
    injeup[i[1]][i[0]] = 1
    # 무방향 인접행렬로 표현해주었음. 방문표시를 하며 순회할 예정
parent = [0]*(N+1) # 각 노드들의 부모 노드를 저장해 줄 리스트
dfs(1)
for i in range(2, len(parent)):
    print(parent[i])

# 메모리 초과가 나는 이유: 인접행렬로 받았기 때문. 노드의 개수가 최대 10만개가 되는데, 이 경우 10만 * 10만짜리 이차원 리스트를 받아와야 하는 경우가
# 생길 수도 있음. 그렇다면? 인접 리스트를 이용하도록 하자