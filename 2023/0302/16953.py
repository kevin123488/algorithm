import sys
sys.stdin = open('16953input.txt')
from collections import deque

def bfs(A, B, cnt, ans): # 현재 수, 목표 수, 시행 횟수
    queue.append((A, cnt))
    while queue:
        start = queue.popleft() # 선입선출의 구조
        if start[0] > B:
            continue
        elif start[0] == B:
            ans = start[1]
            break
        queue.append((start[0]*2, start[1] + 1))
        queue.append((int(str(start[0])+'1'), start[1] + 1))

    return ans

A, B = map(int, input().split())
# 가능한 연산: 2를 곱한다, 1을 수의 오른쪽에 추가한다

ans = 100000000000
queue = deque()
ans = bfs(A, B, 0, ans)
if ans == 100000000000:
    print(-1)
else:
    print(ans + 1)