import sys
sys.stdin = open('1516.txt')
from collections import deque

def topo_sort():
    # num을 시작점으로 하는 위상정렬 알고리즘 수행
    ans_list = []
    while q:
        now_num, stage = q.popleft()
        ans_list.append([now_num, stage])
        for i in building[now_num]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append([i, stage + 1])

    return ans_list

n = int(input())

# 특정 건물을 짓기 위해 먼저 지어야 하는 건물이 있을 수 있음
# 여러개의 건물을 동시에 지을 수 있음

# 진입차수
building = [[] for _ in range(n + 1)] # 1번째 건물을 짓기 위해 먼저 지을 필요가 있는 건물 -> building[1]
in_degree = [0] * (n + 1) # i번째 건물의 진입차수 -> in_degree[i]
building_time = [0] * (n + 1) # building_time[i] = i번 건물을 짓는데 필요한 시간
for i in range(1, n + 1):
    build_list = list(map(int, input().split()))
    building_time[i] = build_list[0]

    for j in range(1, len(build_list)):
        if build_list[j] == -1:
            break
        else:
            building[build_list[j]].append(i)
            in_degree[i] += 1

q = deque()
# 진입차수 0인 곳에서 시작
for i in range(1, n + 1):
    if in_degree[i] == 0: # 진입차수가 0인 시작점
        q.append([i, 0])

ans = topo_sort()
print(ans)

building_time_ans = [0] * (n + 1)

now_ans = 0
now_stage = 0

# 각 건물별로 건축시간을 계산해야 함
# 먼저 스테이지별로 건축시간 start값을 계산해두자.
# 가령 스테이지 0인 건축물은 해당 건축물을 짓는데 필요한 시간을 계산하면 된다.
# 스테이지 1인 건축물은 0인 건축물 중 가장 시간이 오래걸리는 시간 + 해당 건물을 짓는데 걸리는 시간을 더해주면 된다.
# 스테이지 2인 건축물은 1인 건축물 중 가장 시간이 오래걸리는 시간 + 해당 건물을 짓는데 걸리는 시간을 더해주면 된다.

now_stage = 0 # 현재 몇 스테이지를 지나왔는지. 가령 현재 스테이지 1인 건축물을 짓고 있다면 해당 값은 1
now_stage_sum = 0 # 현재 건물을 짓기 위해 필요한 이전단계의 합. 가령 현재 스테이지 1인 건축물을 짓고 있다면 스테이지0인 건툭물 중 가장 오래걸리는 것 ㄱ
now_ans = 0 # 현재 건물을 짓는데 필요한 시간
for i in range(n):
    print(now_stage_sum)
    now_building, stage = ans[i]
    # [건물번호, 스테이지]
    if stage == now_stage:
        now_ans = now_stage_sum + building_time[now_building]
    else:
        now_stage_sum = max(building_time_ans)
        now_ans = now_stage_sum + building_time[now_building]
        now_stage = stage

    building_time_ans[now_building] = now_ans

for i in range(1, n + 1):
    print(building_time_ans[i])

# DP로 풀어야 최솟값이 나옴
# 내가 푼 방식은 선수 건물 관계를 만족시키는 방법 중 하나를 보여주는 것일 뿐, 각 건물들의 건축 시간 최소를 반환해주지는 않음