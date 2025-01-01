import sys
sys.setrecursionlimit(1000000)

def cnt_visited(visited, n):
    cnt = 0
    for i in visited:
        if i == 1:
            cnt += 1
    
    return abs(n - cnt - cnt)


def dfs(n, wires, visited, i, now_node, link_list):
    # 노드 개수, 연결 정보, 방문기록, 끊을 선(wires), 방문중인 노드, 연결된 노드
    # wires[i]에 해당하는 연결을 끊었을 경우 노드가 어떻게 연결될 지 확인 필요
    # 1번 노드에서 시작해서 연결되어있는 노드의 수 확인하자
    # 연결 안되는 것
    non_link_a, non_link_b = wires[i]
    for j in range(1, n + 1): # 현재 노드에서 이동 가능한 애들 ㄱㄱ
        if link_list[now_node][j] == 1:
            if now_node == non_link_a and j == non_link_b or now_node == non_link_b and j == non_link_a:
                continue
            elif visited[j - 1] == 0:
                visited[j - 1] = 1
                dfs(n, wires, visited, i, j, link_list)


    

def solution(n, wires):
    answer = 10000
    # wires 순회하며 하나씩 끊은 상태로 생기는 노드 덩어리를 확인
    # 해당 노드 덩어리(2개)의 노드 개수 차이를 확인하자
    # [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    link_list = [[0] * (n + 1) for _ in range(n + 1)] # 노드간의 연결 정보를 저장
    for i in wires:
        link_list[i[0]][i[1]] = 1
        link_list[i[1]][i[0]] = 1
    
    for i in range(n - 1):
        visited = [0] * n
        visited[0] = 1
        dfs(n, wires, visited, i, 1, link_list)
        answer = min(answer, cnt_visited(visited, n))
        
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

print(solution(n, wires))