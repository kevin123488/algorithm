import sys
sys.stdin = open('12851_input.txt')
from collections import deque
from copy import deepcopy

def bfs(n, k, visited):
    q = deque()
    visited[n] = 1 # 방문기록 체크
    q.append([n, 0, visited]) # 현재 수빈이의 위치와 이동 횟수, 그리고 방문 기록 넣음
    moved_ans = 1000000
    return_ans = 0
    move_list = [1, -1, 2]
    all_length = len(visited)

    while q:
        now, moved, now_visited = q.popleft()
        if now == k:
            if moved <= moved_ans:
                moved_ans = moved
                return_ans += 1
            else:
                return moved_ans, return_ans
        
        for i in range(3): # 현재 위치에서 이동 가능한 방법은 총 3가지
            if move_list[i] == 1 and 0 <= now + 1 < all_length and visited[now + 1] == 0:
                n_now = now + 1
                # now_visited_1 = deepcopy(now_visited)
                now_visited_1 = now_visited[:]
                now_visited_1[n_now] = 1
                q.append([n_now, moved + 1, now_visited_1])

            elif move_list[i] == -1 and 0 <= now - 1 <= all_length and visited[now - 1] == 0:
                n_now = now - 1
                # now_visited_1 = deepcopy(now_visited)
                now_visited_1 = now_visited[:]
                now_visited_1[n_now] = 1
                q.append([n_now, moved + 1, now_visited_1])

            elif move_list[i] == 2 and 0 <= now * 2 <= all_length and visited[now * 2] == 0:
                n_now = now * 2
                # now_visited_1 = deepcopy(now_visited)
                now_visited_1 = now_visited[:]
                now_visited_1[n_now] = 1
                q.append([n_now, moved + 1, now_visited_1])

n, k = map(int, input().split()) # n: 수빈이 위치, k: 동생 위치

# 수빈이는 1초 후 n + 1 혹은 n - 1로 이동 가능
# 순간이동 할 경우 1초 후 2*n의 위치로 이동
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초 후인가? 그리고 그 방법의 가짓수는?

# 방문기록 필요
# 동생의 위치 * 2를 범위의 끝으로 두자
# 5 -> 10 -> 20 -> 19 -> 18
# 5 -> 4 -> 8 -> 16 -> 17
# 5 -> 10 -> 9 -> 18 -> 17

visited = [0] * (2 * max(n, k) + 1)
answer_moved, answer_type = bfs(n, k, visited)


print(answer_moved)
print(answer_type)