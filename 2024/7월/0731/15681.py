import sys
sys.stdin = open('15681.txt')
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

def find_subnode(n, r): # n: 정점의 수, r: 루트의 번호
    visited[r] = 1 # 현재 탐색중인 정점을 우선적으로 카운트
    for i in tree[r]:
        if visited[i] == False:
            visited[r] += find_subnode(n, i)
    
    return visited[r]

n, r, q = map(int, input().split()) # n: 정점의 수, r: 루트의 번호, q: 쿼리 수
gan_seun = [list(map(int, input().split())) for _ in range(n - 1)]

# print(n, r, q, gan_seun)
# 정점 U를 루트로 하는 서브트리에 속한 정점의 수 출력
# 우선 정점 r을 루트로 하는 트리를 리스트 형태로 구현할 필요가 있음 

tree = [[] for _ in range(n + 1)] # 정점은 1번부터 n번까지 이므로 정점 번호와 인덱스 일치시켜주기 위함
for i in gan_seun:
    tree[i[0]].append(i[1])
    tree[i[1]].append(i[0])

# print(tree)
visited = [False for _ in range(n + 1)]

find_subnode(n, r)

for i in range(q):
    u = int(input())
    print(visited[u])