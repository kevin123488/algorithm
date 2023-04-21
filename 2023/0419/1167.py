import sys
from collections import deque
sys.stdin = open('input1167.txt')
input = sys.stdin.readline

# 트리의 지름을 구하자
# 딕셔너리를 활용해 트리 구현

def find_ans(n):
    ans = 0
    q = deque()
    visited = [0] * (v + 1)
    visited[n] = 1
    q.append([n, ans])
    while q:
        now_node, now_ans = q.popleft()
        if now_ans > ans:
            ans = now_ans
        for i in tree[now_node]:
            if visited[i[0]] == 0:
                visited[i[0]] = 1
                q.append([i[0], now_ans + i[1]])

    return ans

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

ans = 0
for i in range(1, v + 1):
    ans = max(find_ans(i), ans)

print(ans)