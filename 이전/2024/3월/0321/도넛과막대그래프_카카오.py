# 크기 n 도넛모양 그래프 -> n개 정점, n개 간선. n각형
# 크기 n 막대모양 그래프 -> n개 정점, n - 1개 간선. 일렬로 쭉 이음
# 크기 n 8자모양 그래프 -> 2n + 1개 정점, 2n + 2개 간선. 크기 n인 도넛모양 그래프에서 정점 하나씩 골라 결합
# 도넛, 막대, 8자모양 그래프가 여럿 있음. 이 그래프들과 무관한 정점 하나 생성 후 각 도넛, 막대, 8자 그래프의 임의 정점으로 향하는 간선 연결
# 그 후 각 정점에 각기 다른 번호 부여
# 그래프의 간선 정보가 주어질 경우 생성한 정점의 번호와 정점을 생성하기 전 도넛 모양 그래프의 수, 막대 모양 및 8자 모양 그래프의 수를 구해야 함
# 2개 이상 다른 곳으로 뻗는 화살표가 있으면서 받는 화살표는 없는 노드 -> 생성한 정점
# 8자 그래프의 개수 -> 다른 곳으로 향하는 화살표 2개, 받는 화살표 2개인 노드의 개수
# 막대 그래프의 개수 -> 아무곳으로도 향하지 않는 노드의 개수
# 도넛 그래프의 개수 -> 생성한 정점에서 뻗어나가는 화살표 수 - (8자 + 막대)

def solution(edges):
    answer = []
    node_line = {}

    for i in edges:
        try:
            node_line[i[0]][0].append(i[1]) # [2, 3]의 경우 node_line[2]의 첫번째 칸에 3 넣어두기 -> 첫번째 칸은 해당 노드로부터 뻗어나가는 대상
        except:
            node_line[i[0]] = [[], []]
            node_line[i[0]][0].append(i[1]) # [2, 3]의 경우 node_line[2]의 첫번째 칸에 3 넣어두기 -> 첫번째 칸은 해당 노드로부터 뻗어나가는 대상

        try:
            node_line[i[1]][1].append(i[0]) # [2, 3]의 경우 node_line[3]의 두번째 칸에 2 넣어두기 -> 두번째 칸은 해당 노드로 들어오는 대상
        except:
            node_line[i[1]] = [[], []]
            node_line[i[1]][1].append(i[0]) # [2, 3]의 경우 node_line[3]의 두번째 칸에 2 넣어두기 -> 두번째 칸은 해당 노드로 들어오는 대상

    mak = 0
    eight = 0
    don = 0
    center_node = 0
    center_node_arrow = 0
    
    for i in node_line:
        now_idx = i
        now_list = node_line[now_idx]
        get_out = len(now_list[0])
        get_in = len(now_list[1])

        if get_out >= 2 and get_in == 0:
            center_node_arrow = get_out
            center_node = now_idx # 추가한 노드에서 뻗어나가는 화살표 수
        
        if get_out == 2 and get_in >= 2:
            eight += 1

        if get_out == 0:
            mak += 1

    don = center_node_arrow - (eight + mak)
    answer = [center_node, don, mak, eight]

    return answer

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
ans = solution(edges)
print(ans)