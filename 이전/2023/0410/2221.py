from collections import deque

n = int(input())
parent = list(map(int, input().split()))

# 각 노드의 진입 차수 계산
in_degree = [0] * (n+1)
for i in range(1, n+1):
    if parent[i-1] != -1:
        in_degree[parent[i-1]] += 1

# 큐에 진입 차수가 0인 노드 추가
queue = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

# 위상 정렬 수행
time = [0] * (n+1)
while queue:
    now = queue.popleft()
    # 직속 상사 중 가장 오래 걸린 시간에 자신의 작업 시간을 더함
    max_time = 0
    for i in range(1, n+1):
        if parent[i-1] == now:
            max_time = max(max_time, time[i])
    time[now] = max_time + 1
    # 다음 노드 처리
    for i in range(1, n+1):
        if parent[i-1] == now:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

# 전체 작업 완료 시간 출력
print(max(time))

# 해고할 수 있는 직원의 최대 수 계산
fire_count = 0
for i in range(1, n+1):
    # 자신의 직속 하사가 모두 해고된 경우
    if parent[i-1] != -1 and time[parent[i-1]] == time[i]:
        fire_count += 1
print(fire_count)