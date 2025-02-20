import sys
from collections import deque
sys.stdin = open('input_17070.txt')

def bfs():
    q = deque()
    q.append([0, 1, 0]) # [행, 열, 형태], 형태: 0(가로), 1(세로), 2(대각선)
    # 행과 열은 기둥의 끝 좌표 기준
    
    ans_cnt = 0

    while q:
        now_i, now_j, now_form = q.popleft()
        if now_i == n - 1 and now_j == n - 1:
            ans_cnt += 1

        # 형태에 따라 이동 가능한 모양이 다름
        if now_form == 0: # 가로 형태
            # 한 칸 앞으로 가기
            if now_j + 1 < n and board[now_i][now_j + 1] == 0:
                q.append([now_i, now_j + 1, 0])
                # 한 칸 앞으로 간 후 45도 기울이기
                if now_i + 1 < n and board[now_i + 1][now_j + 1] == 0 and board[now_i + 1][now_j] == 0:
                    q.append([now_i + 1, now_j + 1, 2])

        elif now_form == 1: # 세로 형태
            if now_i + 1 < n and board[now_i + 1][now_j] == 0:
                q.append([now_i + 1, now_j, 1])
                if now_j + 1 < n and board[now_i + 1][now_j + 1] == 0 and board[now_i][now_j + 1] == 0:
                    q.append([now_i + 1, now_j + 1, 2])
        else: # 대각선 형태
            if now_j + 1 < n and board[now_i][now_j + 1] == 0:
                q.append([now_i, now_j + 1, 0])
            if now_i + 1 < n and board[now_i + 1][now_j] == 0:
                q.append([now_i + 1, now_j, 1])
            if now_i + 1 < n and now_j + 1 < n and board[now_i + 1][now_j + 1] == 0 and board[now_i + 1][now_j] == 0 and board[now_i][now_j + 1] == 0:
                q.append([now_i + 1, now_j + 1, 2])
    
    return ans_cnt

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 벽은 1, 이동 가능한 공간은 0
print(bfs())