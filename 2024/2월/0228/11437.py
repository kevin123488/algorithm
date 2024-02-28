import sys
sys.setrecursionlimit(100000)
sys.stdin = open('11437.txt')

# 깊이 함수
def dfs(node, depth):
    check_nod[node] = 1
    depth_nod[node] = depth

    for i in tree_nod[node]:
        if check_nod[i] == 1:
            continue
        parent_nod[i] = node
        dfs(i, depth + 1)

# 최소 공통 조상 함수
def lca(x, y):
    while depth_nod[x] != depth_nod[y]:
        if depth_nod[x] > depth_nod[y]:
            x = parent_nod[x]
        else:
            y = parent_nod[y]
    
    while x != y:
        x = parent_nod[x]
        y = parent_nod[y]
    
    return x

n = int(input())

# 1번 자리에 1번 노드와 연결된 정보 들어가도록 하자
tree_nod = [[] for _ in range(n + 1)]
parent_nod = [0] * (n + 1) # 부모 노드 정보 저장 리스트
depth_nod = [0] * (n + 1) # 각 노드까지의 깊이
check_nod = [0] * (n + 1) # 노드까지의 길이가 계산되었는지 여부 체크

for i in range(n - 1):
    a, b = map(int, input().split())
    tree_nod[a].append(b)
    tree_nod[b].append(a)

dfs(1, 0) # 1번 노드는 깊이가 1

m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    ans = lca(x, y)
    print(ans)