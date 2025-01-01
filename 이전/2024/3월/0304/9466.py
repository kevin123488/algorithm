import sys
from collections import deque
sys.stdin = open('9466.txt')

def topo_sort(n):
    ans_list = []
    while q:
        ni = q.popleft()
        ans_list.append(ni)
        for i in team_prefer[ni]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    
    return ans_list

t = int(input())
for tc in range(t):
    n = int(input())
    prefer_list = list(map(int, input().split()))
    in_degree = [0] * (n + 1)

    # 팀 구성 조건: 사이클 형성
    # 위상정렬로 사이클 여부를 판단 가능함

    team_prefer = [[] for _ in range(n + 1)]
    for i in range(n):
        team_prefer[i + 1].append(prefer_list[i])
        in_degree[prefer_list[i]] += 1

    q = deque()

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
    
    ans = topo_sort(n)

    print(len(ans))