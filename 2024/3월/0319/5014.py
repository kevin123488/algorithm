import sys
sys.stdin = open('5014.txt')
from collections import deque

def bfs(f, s, g, u, d):
    q.append([s, 0]) # 현재 있는 층 추가, 현재 있는 층에 도달하기 위해 이동한 횟수 추가

    while q:
        now_stage, now_ans = q.popleft() # now_stage: 지금 몇 층, now_ans: 지금 몇 번 이동했는지
        if now_stage == g:
            return now_ans
        
        go_up_stage = now_stage + u
        go_down_stage = now_stage - d

        if 1 <= go_up_stage <= f and visited[go_up_stage] == 0:
            q.append([go_up_stage, now_ans + 1])
            visited[go_up_stage] = 1 # 방문기록 체크 -> 꺼낼때 방문체크 하지 말고 기웃거릴 때 방문체크 하자

        if 1 <= go_down_stage <= f and visited[go_down_stage] == 0:
            q.append([go_down_stage, now_ans + 1])
            visited[go_down_stage] = 1 # 방문기록 체크

    return 'use the stairs'

f, s, g, u, d = map(int, input().split())

# f: 건물 층수
# g: 스타트링크 있는 층수
# s: 강호가 있는 층
# u: 위로 U층만큼
# d: 아래로 D층만큼
# u층 위 혹은 d층 아래에 존재하는 층이 없다 -> 엘리베이터는 이동하지 않음

# 강호가 g층에 도착하기 위해 최소 몇 번을 눌러야 하는가?
# 엘리베이터로 이동 불가면 'use the stairs' 출력

building = [0] * (f + 1)
visited = [0] * (f + 1)
q = deque()

print(bfs(f, s, g, u, d))