import sys
from collections import deque
sys.stdin = open('input17070.txt')
input = sys.stdin.readline

def bfs():
    cnt = 0
    q = deque()
    q.append([[0, 0], [0, 1]])
    while q:
        left_end, right_end = q.popleft()
        if right_end[0] == n-1 and right_end[1] == n-1:
            cnt += 1
        # 밀 수 있는 방법이 총 3가지가 있음
        # 파이프의 형태에 따라 다른 로직을 사용하자
        if left_end[0] == right_end[0] and left_end[1] + 1 == right_end[1]: # 수평
            if 0 <= left_end[0] < n and 0 <= right_end[1] + 1 < n and room[left_end[0]][right_end[1] + 1] == 0:
                q.append([[left_end[0], right_end[1]], [left_end[0], right_end[1] + 1]])
            if 0 <= right_end[0] + 1 < n and 0 <= right_end[1] + 1 < n and room[left_end[0]][right_end[1] + 1] == 0 and room[right_end[0] + 1][right_end[1] + 1] == 0 and room[right_end[0] + 1][right_end[1]] == 0:
                q.append([[right_end[0], right_end[1]], [right_end[0] + 1, right_end[1] + 1]])

        elif left_end[0] + 1 == right_end[0] and left_end[1] + 1 == right_end[1]: # 대각선
            if 0 <= right_end[0] < n and 0 <= right_end[1] + 1 < n and room[right_end[0]][right_end[1] + 1] == 0:
                q.append([[right_end[0], right_end[1]], [right_end[0], right_end[1] + 1]])
            if 0 <= right_end[0] + 1 < n and 0 <= right_end[1] < n and room[right_end[0] + 1][right_end[1]] == 0:
                q.append([[right_end[0], right_end[1]], [right_end[0] + 1, right_end[1]]])
            if 0 <= right_end[0] + 1 < n and 0 <= right_end[1] + 1 < n and room[right_end[0]][right_end[1] + 1] == 0 and room[right_end[0] + 1][right_end[1]] == 0 and room[right_end[0] + 1][right_end[1] + 1] == 0:
                q.append([[right_end[0], right_end[1]], [right_end[0] + 1, right_end[1] + 1]])

        elif left_end[0] + 1 == right_end[0] and left_end[1] == right_end[1]: # 수직
            if 0 <= right_end[0] + 1 < n and 0 <= right_end[1] < n and room[right_end[0] + 1][right_end[1]] == 0:
                q.append([[right_end[0], right_end[1]], [right_end[0] + 1, right_end[1]]])
            if 0 <= right_end[0] + 1 < n and 0 <= right_end[1] + 1 < n and room[right_end[0]][right_end[1] + 1] == 0 and room[right_end[0] + 1][right_end[1]] == 0 and room[right_end[0] + 1][right_end[1] + 1] == 0:
                q.append([[right_end[0], right_end[1]], [right_end[0] + 1, right_end[1] + 1]])

    return cnt

n = int(input())
# 각 칸은 빈 칸이거나 벽
# 파이프는 연속된 2개의 칸을 차지함
# 파이프는 회전이 가능하며, -, ㅣ, 왼쪽 위에서 오른쪽 아래를 가로지르는 방향 총 3가지가 가능함
# 파이프는 항상 빈 칸만 차지해야 한다.
# 파이프는 밀어서 이동시키며, 위에서 아래로, 왼쪽에서 오른쪽으로, 왼쪽 위에서 오른쪽 아래로 밀 수 있다
# 이동의 개념은 끝 부분(파이프가 차지중인 인덱스중 i에 해당하는 값이 더 큰 쪽)의 위치를
# 해당 칸보다 한 칸 전진시키는 것

room = [list(map(int, input().split())) for _ in range(n)]
print(bfs())