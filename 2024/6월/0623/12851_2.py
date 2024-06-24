# 메모리 초과 해소용 답안
import sys
sys.stdin = open('12851_input.txt')
from collections import deque

def bfs(n, k):
    q = deque()
    max_length = max(n, k) * 2 + 1  # 충분히 큰 범위 설정
    visited = [-1] * max_length  # 방문 횟수를 저장 (-1은 방문하지 않은 상태)
    q.append((n, 0))  # (현재 위치, 이동 횟수)
    visited[n] = 0
    min_moves = float('inf')
    ways = 0

    while q:
        now, moves = q.popleft()
        
        if now == k:
            if moves < min_moves:
                min_moves = moves
                ways = 1
            elif moves == min_moves:
                ways += 1
            continue

        next_positions = [now + 1, now - 1, now * 2]
        for next_pos in next_positions:
            if 0 <= next_pos < max_length:
                # 다음 위치를 방문하지 않았거나, 더 적은 이동 횟수로 방문할 수 있는 경우
                if visited[next_pos] == -1 or visited[next_pos] >= moves + 1:
                    visited[next_pos] = moves + 1
                    q.append((next_pos, moves + 1))

    return min_moves, ways

n, k = map(int, input().split())  # n: 수빈이 위치, k: 동생 위치

answer_moved, answer_type = bfs(n, k)

print(answer_moved)
print(answer_type)