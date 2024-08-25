import sys
sys.stdin = open('20040.txt')
sys.setrecursionlimit(1000000)

def find_parent(parents, now_node):
    # 루트 찾을 때 까지 재귀호출
    if parents[now_node] != now_node:
        parents[now_node] = find_parent(parents, parents[now_node])
    
    return parents[now_node]

def union_parent(parents, start_node, fin_node):
    start_node = find_parent(parents, start_node)
    fin_node = find_parent(parents, fin_node)

    if start_node > fin_node:
        parents[start_node] = fin_node
    
    else:
        parents[fin_node] = start_node

n, m = map(int, input().split())
parents = [i for i in range(n)]

flag = 0
for i in range(1, m + 1):
    start_node, fin_node = map(int, input().split())

    if find_parent(parents, start_node) == find_parent(parents, fin_node):
        print(i)
        flag = 1
        break

    else:
        union_parent(parents, start_node, fin_node)

if flag == 0:
    print(0)