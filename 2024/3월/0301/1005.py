import sys
from collections import deque
sys.stdin = open('1005.txt')

def topology_sort():
    ans_list = []
    while q:
        atom, stage = q.popleft()
        ans_list.append([atom, stage, build_time[atom - 1]])
        for i in building_seq[atom]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append([i, stage + 1])
    ans_list.sort(key=lambda x: x[1])  # 단계별로 정렬
    return ans_list

t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    build_time = list(map(int, input().split()))
    building_seq = [[] for _ in range(n + 1)]

    in_degree = [0] * (n + 1)

    for i in range(k):
        x, y = map(int, input().split()) # x를 지은 뒤에 y 짓는것이 가능
        building_seq[x].append(y)
        in_degree[y] += 1

    q = deque()
    
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append([i, 1])
    
    ans = topology_sort()
    
    w = int(input())
    ans_time = 0
    ans_stage = 0
    
    for i in range(len(ans)):
        if ans[i][0] == w:
            ans_stage = ans[i][1]
    
    ans_stage_list = [[] for _ in range(ans_stage + 1)] # 스테이지별로 가장 큰 값을 구하기 위해 만든 리스트

    for i in range(len(ans)):
        if ans[i][1] < ans_stage:
            ans_stage_list[ans[i][1]].append(ans[i][2])
    
    for i in range(1, ans_stage + 1):
        if ans_stage_list[i]:
            ans_time += max(ans_stage_list[i])
    
    ans_time += build_time[w - 1]

    print(ans_time)