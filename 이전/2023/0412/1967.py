import sys
sys.stdin = open('input1967.txt')
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def tree_find(node, ans):
    global max_ans
    visited[node-1] = 1
    max_ans = max(max_ans, ans)

    # ans += tree[node][0][1]
    # tree_find(tree[node][0][0], ans, max_ans)
    # ans -= tree[node][0][1]
    # ans += tree[node][1][1]
    # tree_find(tree[node][1][0], ans, max_ans)
    # ans -= tree[node][1][1]
    for i in tree[node]:
        if visited[i[0]-1] == 0:
            ans += i[1]
            # visited[i[0]-1] = 1
            tree_find(i[0], ans)
            # visited[i[0]-1] = 0
            ans -= i[1]


# 트리는 사이클이 없는 무방향 그래프이다.
# 두 노드 사이에 한개의 경로만 존재
# 트리에서 어떤 두 노드를 선택해서 양쪽으로 당길 때, 가장 길게 늘어나는 경우가 있을 것.
# 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
# 이 지름은 트리에 존재하는 모든 경로 중 가장 긴 것이다.
# 트리의 지름을 구하자

n = int(input())
tree = {}
for i in range(n-1):
    root, node, value = map(int, input().split())
    try:
        tree[root].append([node, value])
    except:
        tree[root] = [[node, value]]

    try:
        tree[node].append([root, value])
    except:
        tree[node] = [[root, value]]

ans = 0
max_ans = 0
visited = [0] * n
for i in tree:
    visited = [0] * n
    tree_find(i, ans)
print(max_ans)