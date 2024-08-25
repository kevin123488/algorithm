import sys
sys.stdin = open('20040.txt')
input = sys.stdin.readline

def find_parent(num):
    if parent_list[num] != num:
        parent_list[num] = find_parent(parent_list[num])
    
    return parent_list[num]


def union_cycle(start, end):
    # 노드 두 개를 비교함
    # 양 노드의 부모가 동일하면 사이클
    # 양 노드의 부모가 다를 경우 부모를 합쳐주자
    # 더 높은 값의 부모로 통일시켜주자
    start_parent = find_parent(start)
    end_parent = find_parent(end)
    
    if start_parent == end_parent:
        return True
    elif start_parent < end_parent:
        parent_list[end_parent] = start_parent
        return False
    else:
        parent_list[start_parent] = end_parent
        return False


n, m = map(int, input().split())
parent_list = [i for i in range(n)] # 노드별 조상의 정보를 기록하는 리스트. parent_list[0] -> 0번째 노드의 조상
flag = 0
# print(parent_list)
# 사이클 판별은 크게 판별 부분과 합침 부분으로 나눌 수 있다.
for i in range(1, m + 1):
    start, end = map(int, input().split())
    # parent_list[start] = max(end, parent_list[start])
    # parent_list[end] = max(start, parent_list[end])

    cycle_yes_no = union_cycle(start, end)
    if cycle_yes_no == True:
        print(i)
        flag = 1
        break
    else:
        continue
# print(parent_list)
if flag == 0:
    print(0)