import sys
sys.stdin = open('12851_input.txt')
from collections import deque

def bfs(n, k, visited):
    q = deque()
    visited[n] = 1 # 방문기록 체크
    q.append([n, 0]) # 현재 수빈이의 위치와 이동 횟수, 그리고 방문 기록 넣음
    moved_ans = 1000000
    return_ans = 0

    while q:
        now, moved = q.popleft()
        if now == k:
            if moved <= moved_ans:
                moved_ans = moved
                return_ans += 1
            else:
                break
        
        for i in [now + 1, now - 1, now * 2]:
            if 0 <= i < len(visited) and (visited[i] == 0 or visited[i] >= moved + 1):
                visited[i] = moved + 1
                q.append([i, moved + 1])

    return moved_ans, return_ans


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
# answer_moved, answer_type = bfs(n, k, visited)

moved, type = bfs(n, k, visited)

print(moved)
print(type)