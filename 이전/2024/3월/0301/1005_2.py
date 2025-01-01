import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('1005.txt')

def topo_sort(building, w):
    q = deque()
    stage_num = 1 # 몇번째 단계에서 해당 건물이 건축되는지 확인
    q.append([building, stage_num, build_time[building - 1]]) # 건물 번호, 몇단계에서 건축 가능한지, 건축 시간
    copy_in_degree = deepcopy(in_degree)
    ans_list = [[] for _ in range(len(build_sequence))] # 스테이지별로 
    last_stage_num = 0

    while q:
        now_building, now_stage_num, now_build_time = q.popleft()
        if now_building == w:
            last_stage_num = now_stage_num
        ans_list[now_stage_num].append(now_build_time)
        for i in build_sequence[now_building]: # 현재 빌딩과 연결되어있는 다른 빌딩
            copy_in_degree[i] -= 1 # 현재 빌딩을 큐에 넣고 연결된 빌딩의 진입차수를 낮춰줘야 함
            print(copy_in_degree[w])
            if copy_in_degree[i] == 0:
                q.append([i, now_stage_num + 1, build_time[i - 1]])
    
    # 4번 건물의 진입차수가 3임. 근데 내가 작성한 코드는 1번 건물에서 시작하는 경우와 5번 건물에서 시작하는 경우로 나뉨.
    # 즉 진입차수를 3번 깎아줘야 4번이 큐에 들어가는데 1번 시작 케이스의 경우 2번, 5번 시작 케이스의 경우 1번 진입차수를
    # 깎아주게 됨. 따라서 진행이 안되는 상황
    
    ans = 0
    for i in range(1, len(ans_list)):
        if len(ans_list[i]) > 0:
            ans += max(ans_list[i])
        elif i == last_stage_num:
            ans += build_time[w - 1] # w는 목표가 되는(마지막에 건설해야 하는) 건물
            break
    
    print(ans)
    return ans


t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    in_degree = [0] * (n + 1)
    build_sequence = [[] for _ in range(n + 1)]
    build_time = list(map(int, input().split()))

    for i in range(k):
        a, b = map(int, input().split())
        build_sequence[a].append(b) # a 지어야 b 짓기 가능
        in_degree[b] += 1 # 진입차수

    w = int(input())

    min_ans = 999999999
    for i in range(1, n + 1):
        if in_degree[i] == 0: # 진입차수가 0인 (시작점이 될 수 있는) 건물
            min_ans = min(topo_sort(i, w), min_ans)
    
    print(min_ans)