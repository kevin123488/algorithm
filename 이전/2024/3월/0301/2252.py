import sys
from collections import deque
sys.stdin = open('2252.txt')

def bfs():
    while q:
        x = q.popleft()
        ans_list.append(x)
        for i in height_list[x]:
            bigger_than[i] -= 1
            if bigger_than[i] == 0:
                q.append(i)

n, m = map(int, input().split())
height_list = [[] for _ in range(n + 1)]
bigger_than = [0] * (n + 1) # 진입차수. 진입차수는 해당 노드에 들어오는 간선의 수를 의미. 
# 진입차수가 0이 되면 해당 노드가 시작점이 됨
q = deque()

# 키 비교 리스트에 값 채워넣기
for i in range(m):
    front_stu, back_stu = map(int, input().split())
    height_list[front_stu].append(back_stu)
    bigger_than[back_stu] += 1 # back_stu와 비교했을 때 앞에 와야한다고 주어진 학생의 수

print(height_list)

for i in range(1, n + 1):
    if bigger_than[i] == 0:
        q.append(i) # 순서 상관 없이 앞에만 적어주면 되는 요소들

ans_list = []

bfs()

for i in ans_list:
    print(i, end=' ')