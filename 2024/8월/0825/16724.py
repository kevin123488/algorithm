import sys
sys.stdin = open('16724.txt')
input = sys.stdin.readline

def find(node):
    if parent_list[node] != node:
        parent_list[node] = find(parent_list[node])
    
    return parent_list[node]

def union(i, j, n, m, where_to_go):
    global answer
    # 현재 좌표의 세로 좌표, 가로 좌표, 지도의 높이, 지도의 폭, move_map[i][j] 에서의 이동 방향
    if empty_map[i][j] == 1:
        return
    empty_map[i][j] = 1
    start_node = m * i + j
    if where_to_go == 'U':
        fin_node = start_node - m
    elif where_to_go == 'D':
        fin_node = start_node + m
    elif where_to_go == 'L':
        fin_node = start_node - 1
    else:
        fin_node = start_node + 1
    
    start_node_parent = find(start_node)
    fin_node_parent = find(fin_node)

    if start_node_parent == fin_node_parent:
        answer += 1
        return # 사이클 존재하는 것
    else:
        if start_node_parent < fin_node_parent: # 부모의 값이 더 작은 쪽을 큰 쪽의 부모로 정함
            parent_list[fin_node_parent] = start_node_parent
        else:
            parent_list[start_node_parent] = fin_node_parent
    
    # 다음 좌표로 이동
    if where_to_go == 'U':
        union(i - 1, j, n, m, move_map[i - 1][j])
    elif where_to_go == 'D':
        union(i + 1, j, n, m, move_map[i + 1][j])
    elif where_to_go == 'L':
        union(i, j - 1, n, m, move_map[i][j - 1])
    else:
        union(i, j + 1, n, m, move_map[i][j + 1])

    return

n, m = map(int, input().split()) # n: 행, m: 열
move_map = [list(input()) for _ in range(n)]
empty_map = [[0] * m for _ in range(n)]

# 피리소리 들리면 회원들은 이동함. 지도에 새겨진 U, D, L, R 문자에 따라 상, 하, 좌 우 이동함
# safe zone에선 피리소리를 들을 수 없음 -> 이동 X
# 영과일 회원들이 지도 어느 부분에 있든 상관 없이 피리소리가 들려올 때 safe zone으로 들어갈 수 있게 하는 safe zone의
# 최소 개수를 출력
# 간단히 말해 지도 어디에 있든 화살표를 따라가다 보면 safe zone에 도달하도록 하는 safe zone의 최소 개수를
# 구하는 문제
# 풀이
# dfs를 활용하여 몇 개의 단락으로 구성되어 있는지 체크하면 됨 -> 단락이 아니라 사이클임

# 지도에 주어진 방향을 간선의 방향이라고 생각하자
# 1단계: 지도를 간선 그래프로 치환
# 2단계: 간선 그래프를 탐색하며 사이클 수 판별


# 각 노드별 부모 노드를 저장하자
parent_list = [i for i in range(n * m)]

answer = 0
for i in range(n):
    for j in range(m):
        if empty_map[i][j] == 0:
            union(i, j, n, m, move_map[i][j])

print(answer)