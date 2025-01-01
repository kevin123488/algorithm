import sys
from collections import deque
sys.stdin = open('1766.txt')

def topo_sort():
    ans_list = []
    while q:
        ni, n_stage = q.popleft()
        ans_list.append([ni, n_stage])
        for i in solve_seq[ni]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append([i, n_stage + 1])
    
    return ans_list

n, m = map(int, input().split())
solve_seq = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    solve_seq[x].append(y)
    in_degree[y] += 1

for i in range(1, n + 1):
    solve_seq[i].sort()
print(in_degree)
print(solve_seq)
q = deque()

for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append([i, 1]) # 시작점은 1단계

ans = topo_sort()

now_stage = 1
print(in_degree)
# 각 문제별로 몇단계에 풀어야 하는지 확인, 단계별로 문제 모아두고 해당 문제들 다시 정렬해서 출력하면 됨 -> 아님.