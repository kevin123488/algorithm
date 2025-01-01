import sys
sys.stdin = open('5021.txt')
from collections import deque

def find_name(now_person):
    for z in name_num_link:
        if name_num_link[z] == now_person:
            return z

def topo_sort():
    ans_list = []
    while q:
        now_person, now_stage = q.popleft()
        now_person_name = find_name(now_person)
        if now_person_name in want_king_list:
            ans_list.append([now_person_name, now_stage])
        
        for k in family_information[now_person]:
            in_degree[k] -= 1
            if in_degree[k] == 0:
                q.append([k, now_stage + 1])

    return ans_list


n, m = map(int, input().split())
king = input()
family_information = [[] for _ in range(3 * n + 1)] # 
in_degree = [0] * (3 * n + 1)
name_num_link = {}

cnt = 1
for i in range(n):
    input_list = input().split()
    child, parent_1, parent_2 = input_list
    
    for j in input_list:
        try:
            name_num_link[j]
        except:
            name_num_link[j] = cnt
            cnt += 1

    family_information[name_num_link[parent_1]].append(name_num_link[child])
    family_information[name_num_link[parent_2]].append(name_num_link[child])
    in_degree[name_num_link[child]] += 2

in_degree = in_degree[:len(name_num_link) + 1]
family_information = family_information[:len(name_num_link) + 1]

ans_cnt = -1
next_king = ''
want_king_list = []
for j in range(m):
    want_king = input()
    want_king_list.append(want_king)

q = deque()
for i in range(1, len(in_degree)):
    if in_degree[i] == 0:
        q.append([i, 0])

# for i in name_num_link:
#     if i == king:
#         king_idx = name_num_link[i]
# print(king_idx)
# q.append([king_idx, 0])

ans = topo_sort()
for i in ans:
    if ans_cnt == -1:
        ans_cnt = i[1]
        next_king = i[0]
    else:
        if ans_cnt < i[1]:
            ans_cnt = i[1]
            next_king = i[0]

print(next_king)

# 위상정렬 사용
# want_king에 도달하기 위해 선수적으로 처리되어야 하는 것 -> parent
# 우선 모든 인원을 숫자에 매핑할 필요가 있음
# 결과를 다시 이름과 매핑하여 리턴하면 됨
