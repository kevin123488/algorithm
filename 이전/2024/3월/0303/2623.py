import sys
sys.stdin = open('2623.txt')
from collections import deque

def topo_sort(n):
    ans_list = []
    while q:
        ni = q.popleft()
        ans_list.append(ni)
        for i in singer_seq[ni]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    
    if len(ans_list) == n:
        return ans_list
    else:
        return 0

n, m = map(int, input().split())
singer_seq = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for i in range(m):
    seq_list = list(map(int, input().split())) # 인덱스 1부터 사용
    # 관건: 입력받은 순서를 이용, singer_seq와 in_degree를 채워줘야 함
    # 사이클 형성하는지 아닌지 판단 필요. 형성하면 0 출력, 그 외엔 순서 출력
    for j in range(1, len(seq_list) - 1): # 0 ~ 2
        for k in range(j + 1, len(seq_list)): # 
            if seq_list[k] not in singer_seq[seq_list[j]]:
                singer_seq[seq_list[j]].append(seq_list[k])
                in_degree[seq_list[k]] += 1

q = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)

ans = topo_sort(n)

if ans == 0:
    print(0)
else:
    for i in ans:
        print(i)