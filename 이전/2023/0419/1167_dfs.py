import sys
from collections import deque
sys.stdin = open('input1167.txt')
input = sys.stdin.readline

# 트리의 지름을 구하자
# 딕셔너리를 활용해 트리 구현

def find_ans(n):
    visited = [0] * (v + 1)
    visited[n] = 1
    stack = deque()
    ans = 0
    stack.append([n, ans])
    max_ans = [0, 0]
    while stack:
        now_node, now_ans = stack.pop()
        if now_ans > max_ans[1]:
            max_ans = [now_node, now_ans]
        for i in tree[now_node]:
            if visited[i[0]] == 0:
                visited[i[0]] = 1
                stack.append([i[0], now_ans + i[1]])

    return max_ans

v = int(input())
tree = [[] for _ in range(v+1)] # 노드 번호와 인덱스를 일치시켜주기 위함
for i in range(v):
    arr = list(map(int, input().split()))
    node = arr[0]
    temp = []
    for j in range(1, len(arr)): # 길이가 7일 때 0~6까지 순회
        if j % 2: # 이어진 노드 정보
            temp = [arr[j]]
        else:
            temp.append(arr[j])
            tree[node].append(temp)



# ans = 0
# for i in range(1, v + 1):
#     ans = max(find_ans(i)[1], ans)

# 노드 지름 구할 깨 아래 방식 사용하는거 기억해두자
# 먼저 1 노드와 가장 먼 거리를 지니는 노드를 탖고
# 그 노드에서 시작해 가장 먼 거리를 가지는 노드를 찾으면 된다
node, ans = find_ans(1)
node, real_ans = find_ans(node)

print(real_ans)