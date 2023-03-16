import sys
sys.stdin = open('input13262.txt')
from collections import deque

def bfs(start):
    global ans
    color = 'red'
    q.append([start, color])
    visited[start] = color
    while q:
        start_point = q.popleft()
        if visited[start_point[0]] == 'green':
            color = 'red'
        else:
            color = 'green'
            # 색을 정해주는 타이밍은 왜 여기여야 하는가?

        for i in range(len(arr[start_point[0]])): # start_point와 연결되어 있는 동그라미를 조회하는 것
            if arr[start_point[0]][i] == 1: # 연결되어 있으면서 방문하지 않았다?
                if visited[i] == 0:
                    visited[i] = color
                    # 방문처리를 해주는 타이밍은 왜 여기여야 하는가?
                    q.append([i, color])
                else:
                    if visited[i] == visited[start_point[0]]: # 현재 타겟인 동그라미와 그 동그라미에 연결된 동그라미의 색이 같다?
                        ans = 'impossible'
                        return


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)] # 인접행렬 사용
    for i in range(m):
        idx, rnd = map(int, input().split())
        arr[idx][rnd] = 1
        arr[rnd][idx] = 1

    visited = [0] * (n+1) # 동그라미 방문리스트
    q = deque()
    ans = 'possible'
    bfs(1)
    for i in range(1, len(visited)):
        if visited[i] == 0:
            bfs(i)

    print(ans)