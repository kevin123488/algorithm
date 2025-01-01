import sys
sys.stdin = open('4386.txt')
import math

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 별의 개수
n = int(input())
star = [0]
for i in range(n):
    a,b = map(float, input().split())
    star.append((a,b))

parent = [i for i in range(n+1)] # 부모 테이블 초기화

# 모든 간선 정보를 입력받기
edges = []
for i in range(1,n):
    for j in range(i+1,n+1):
        cost = math.sqrt((star[i][0]-star[j][0])**2 + (star[i][1]-star[j][1])**2)

        edges.append((cost,i,j))
edges.sort()

result = 0

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result+=cost

print(round(result, 2))