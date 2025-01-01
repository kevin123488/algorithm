from collections import deque
from pprint import pprint

di = [0, 0, 1, -1, 1, -1, 1, -1]
dj = [1, -1, 0, 0, -1, -1, 1, 1]

di_bfs = [0, 0, 1, -1]
dj_bfs = [1, -1, 0, 0]

def fill_paper(under_x, under_y, upper_x, upper_y, paper):
    for i in range(under_x - 1, upper_x): # 인덱스 변환 과정에서 보정
        for j in range(under_y - 1, upper_y):
            paper[i][j] = 1
    
    return paper

def paint_outer(paper):
    for i in range(50):
        for j in range(50):
            if paper[i][j] == 1: # 사각형 범위 내일 때
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < 50 and 0 <= nj < 50 and paper[ni][nj] == 0:
                        paper[i][j] = 2
                        break
                    elif i == 0 or j == 0 or i == 49 or j == 49: # 종이의 끝 부분이라 테두리 확정
                        paper[i][j] = 2
                        break
    
    for i in paper:
        print(i)
    print()
    
    return paper

def find_answer(outer, characterX, characterY, itemX, itemY):
    q = deque()
    return_answer = 0
    q.append([characterX, characterY, return_answer])
    visited = [[False] * 50 for _ in range(50)]
    
    while q:
        now_x, now_y, answer = q.popleft()
        if now_x == itemX and now_y == itemY:
            return_answer = answer
            break
        
        for i in range(4):
            nx = now_x + di_bfs[i]
            ny = now_y + dj_bfs[i]
            if 0 <= nx < 50 and 0 <= ny < 50 and outer[nx][ny] == 2:
                if visited[nx][ny] == False:
                    visited[nx][ny] = answer + 1
                    q.append([nx, ny, answer + 1])
                elif visited[nx][ny] > answer + 1:
                    visited[nx][ny] = answer + 1
                    q.append([nx, ny, answer + 1])
    
    return return_answer
                

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 입력받는 사각형의 범위를 모두 1로 채우자
    # 그 후 주변에 0이 있는 1만 테두리로 간주하면 될 것 같다
    paper = [[0] * 50 for _ in range(50)]
    for i in rectangle:
        under_x, under_y, upper_x, upper_y = i
        paper = fill_paper(under_x, under_y, upper_x, upper_y, paper)
    
    outer = paint_outer(paper)
    answer = find_answer(outer, characterX - 1, characterY - 1, itemX - 1, itemY - 1)

    print(answer)    
    return answer

rectangle = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8

solution(rectangle, characterX, characterY, itemX, itemY)