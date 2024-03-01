import sys
from collections import deque
sys.stdin = open('14567.txt')

n, m = map(int, input().split())
before_subject = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    before_subject[a].append(b) # a번 인덱스에 b과목 추가 -> a과목이 b과목의 선수과목. a가 b보다 순서가 먼저여야 함
    in_degree[b] += 1

q = deque()
# 시작점이 될 수 있는 요소 q에 넣기
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append([i, 1])

ans_list = []
semester = 1
while q:
    x, seme = q.popleft()
    ans_list.append([x, seme])
    for i in before_subject[x]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append([i, seme + 1])

# 1, 4, 6, 2, 3, 5 순으로 들어야 함. 입력받은 1 2, 1 3, 2 5, 4 5 가지고 몇학기에 걸쳐 들어야하는지 판단 필요
ans_list.sort()
for i in ans_list:
    print(i[1], end=' ')