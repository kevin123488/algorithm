import sys
sys.stdin = open('input_1707.txt')
sys.setrecursionlimit(100000)

def dfs(now_node, visited, injeup_list, group):
    visited[now_node] = group # 현재 노드에 대해 설정한 그룹의 값을 넣어줌

    for i in injeup_list[now_node]:
        if visited[i] == 0:
            if dfs(i, visited, injeup_list, group * (-1)) == False:
                return False
        elif visited[i] == group:
            return False
    
    return True


k = int(input())
# 간선 정보에 맞게 색을 칠해가면서 dfs 진행
# 만약 색칠하려 하는 칸에 적용되어야 하는 색과 반대되는 색이 이미 칠해져있다? 이분그래프 아닌 것
for i in range(k):
    v, e = map(int, input().split()) # 정점의 개수, 간선의 개수
    injeup_list = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for j in range(e):
        start_node, end_node = map(int, input().split())
        injeup_list[start_node].append(end_node)
        injeup_list[end_node].append(start_node)

    for l in range(1, v + 1):
        if visited[l] == 0:
            result = dfs(l, visited, injeup_list, 1)
            if result == False:
                break
    
    if result == False:
        print('NO')
    else:
        print('YES')