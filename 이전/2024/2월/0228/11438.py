import sys
sys.stdin = open('11438.txt')
sys.setrecursionlimit(100000)

# 11437문제와 같이 lca 알고리즘을 사용하나 시간복잡도를 개선해야 함

# 깊이 계산 함수
def dfs(node, depth):
    check_nod[node] = 1
    depth_nod[node] = depth

    for i in tree_nod[node]:
        if check_nod[i] == 1:
            continue
        parent_nod[i] = node
        dfs(i, depth + 1)

# lca 함수
def lca(x, y):
    # 노드 x와 y의 깊이를 맞춰주는 과정이 필요
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
tree_nod = [[] for _ in range(n + 1)]
depth_nod = [0] * (n + 1)
parent_nod = [0] * (n + 1)
check_nod = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())
    tree_nod[a].append(b) # a 인덱스에 해당하는 리스트에 b값 넣기 -> a와 b가 연결되어있음을 의미
    tree_nod[b].append(a)

dfs(1, 0)

m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    ans = lca(x, y)
    print(ans)