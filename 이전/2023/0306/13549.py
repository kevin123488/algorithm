import sys
sys.stdin = open('13549input.txt')
from collections import deque

def bfs(N, K, ans):
    q.append([N, 0]) # 수빈이의 위치와 지난 시간을 입력
    while q:
        start = q.popleft()
        visited[start[0]] = 1
        if 0 <= start[0]*2 <= 2 * max(N, K) and visited[start[0]*2] == 0:
            q.append([start[0]*2, start[1]])
        if 0 <= start[0]-1 <= 2 * max(N, K) and visited[start[0]-1] == 0:
            q.append([start[0]-1, start[1] + 1])
        if 0 <= start[0]+1 <= 2 * max(N, K) and visited[start[0]+1] == 0:
            q.append([start[0]+1, start[1] + 1])

        if start[0] == K and start[1] < ans:
            ans = start[1]

    return ans


N, K = map(int, input().split())
# 수빈이는 N에 위치, 동생은 K에 위치
# 수빈이는 걷거나 순간이동 가능
# 위치 X에서 걸으면 1초 후 X+1 혹은 X-1 위치로 이동
# 순간이동을 하는 경우 0초 후 2*X의 위치로 이동
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램 작성
# 완전탐색을 하기엔 방문기록을 체크할 수 없기 떄문에 살짝 무리가 있다.
# 범위를 0부터 K와 N중 더 큰 값까지로 두면 될 것
# 메모리 넉넉하니 해당 부분을 방문체크로 둬도 될 것 같다.

visited = [0 for _ in range(2 * max(N, K) + 1)] # 위치에 해당하는 숫자와 인덱스를 맞춰주기 위함
# print(visited)
q = deque()
ans = 10**9
print(bfs(N, K, ans))