import sys
sys.stdin = open('4386.txt')
import math

def find_parent(a): # 부모 별을 찾는 함수
    # if parent[a] == a:
    #     return a
    
    # else:
    #     return find_parent(parent[a])
    while True:
        if parent[a] == a:
            break
        else:
            a = parent[a]
        
    return a



def union_parent(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if parent_a > parent_b: # 두 별의 부모 별을 똑같이 맞춰주는 과정. 더 작은 값을 부모로 삼도록 만들자
        parent[a] = parent_b
    else:
        parent[b] = parent_a


n = int(input())
star = [list(map(float, input().split())) for _ in range(n)]

parent = [i for i in range(n)]

# 간선정보 저장
star_line_list = []
for i in range(n - 1):
    for j in range(i, n):
        front_star = star[i]
        back_star = star[j]
        fee = math.sqrt((front_star[0] - back_star[0])**2 + (front_star[1] - back_star[1])**2)

        star_line_list.append([fee, i, j])

star_line_list.sort()

ans = 0
cnt = 0
for i in star_line_list:
    a = i[1]
    b = i[2]
    if find_parent(a) != find_parent(b): # 간선 연결 가능
        union_parent(a, b) # 간선 연결
        ans += i[0]
        cnt += 1
    
    if cnt == n - 1:
        break

print(float(round(ans, 2)))