# 위상정렬 빠르게 복습
import sys
sys.stdin = open('2252_input.txt')
from collections import deque

def topo_sort(q):
    ans_list = []
    while q:
        now_stu = q.popleft()
        ans_list.append(now_stu)
        for i in stu_list[now_stu]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    return ans_list

n, m = map(int, input().split())
in_degree = [0] * (n + 1) # 학생수 + 1만큼 칸을 만들어두자. 학생 번호와 인덱스를 일치시켜주기 위함
stu_list = [[] for _ in range(n + 1)]
for i in range(m):
    front_stu, back_stu = map(int, input().split())
    in_degree[back_stu] += 1
    stu_list[front_stu].append(back_stu)

q = deque()

for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)

answer = topo_sort(q)

for i in answer:
    print(i, end=' ')