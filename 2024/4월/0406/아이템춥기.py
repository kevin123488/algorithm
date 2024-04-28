from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(board, characterX, characterY, itemX, itemY):
    q = deque()
    q.append([characterX, characterY, 0])
    visited = [[0] * 51 for _ in range(51)]
    while q:
        now_x, now_y, cnt = q.popleft()
        if now_x == itemX and now_y == itemY:
            return cnt
        
        for i in range(4):
            ni = now_x + di[i]
            nj = now_y + dj[i]
            if 0 <= ni <= 50 and 0 <= nj <= 50 and board[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj, cnt + 1])
    

def paint_board(rec, board):
    x_small, y_small, x_big, y_big = rec
    for i in range(51):
        for j in range(51):
            if x_small <= i <= x_big and y_small <= j <= y_big:
                board[i][j] = 2

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 직사각형 별로 내부를 2
    # 그 후 0과 맞물려있는 애들을 1로 바꾸자
    # 탐색시 1인 애들만 하면 ㄴㅇㅅ
    
    # x축 y축 모두 0, 0에서 시작함
    # 판 생성
    board = [[0] * 51 for _ in range(51)]
    
    # 사각형 좌표 입력받을 때
    for rec in rectangle:
        paint_board(rec, board)
    
    # 사각형 테두리만 남기기
    for i in range(51):
        for j in range(51):
            if board[i][j] == 2:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni <= 50 and 0 <= nj <= 50 and board[ni][nj] == 0:
                        # board[i][j] -> 테두리
                        board[i][j] = 1
                        break
    
    answer = bfs(board, characterX, characterY, itemX, itemY)
    for i in board:
        print(i)
            
    return answer

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8

print(solution(rectangle, characterX, characterY, itemX, itemY))