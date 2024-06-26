import sys
sys.stdin = open('input_2239.txt')
# 출처 -> https://www.acmicpc.net/problem/2239

def row_check(r, num): # 행
    for i in range(9):
        if sudoku[r][i] == num:
            return False
    
    return True

def col_check(c, num): # 열
    for i in range(9):
        if sudoku[i][c] == num:
            return False
        
    return True

def seq_check(r, c, num): # 사각형
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[nr + i][nc + j] == num:
                return False
    
    return True


def backtracking(depth): # 백트래킹 함수
    if depth >= len(z_list):
        for k in sudoku:
            temp_ans = ''
            for z in k:
                temp_ans += str(z)
            print(temp_ans)
        exit()
    
    nr, nc = z_list[depth]
    for i in range(1, 10):
        if col_check(nc, i) and row_check(nr, i) and seq_check(nr, nc, i):
            sudoku[nr][nc] = i
            backtracking(depth + 1)
            sudoku[nr][nc] = 0

sudoku = [list(map(int, input())) for _ in range(9)]
z_list = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            z_list.append([i, j]) # 값을 넣어줘야 하는 보드판 좌표 기록

backtracking(0)