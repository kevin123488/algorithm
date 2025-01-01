import sys
from pprint import pprint
sys.stdin = open('2239_input.txt')

def check_sero(a): # 스도쿠 세로줄이 스도쿠 만족하는지
    # 카운트하며 나온 숫자가 또 나올 경우 return -1
    num_list = []
    for i in range(9):
        if sudoku[i][a] == 0:
            continue
        if num_list == []:
            num_list.append(sudoku[i][a])
        else:
            if sudoku[i][a] in num_list:
                return -1
            else:
                num_list.append(sudoku[i][a])
    return 1

def check_garo(b): # 스도쿠 가로줄이 스도쿠 만족하는지
    # 카운트하며 나온 숫자가 또 나올 경우 return -1
    num_list = []
    for i in range(9):
        if sudoku[b][i] == 0:
            continue
        if num_list == []:
            num_list.append(sudoku[b][i])
        else:
            if sudoku[b][i] in num_list:
                return -1
            else:
                num_list.append(sudoku[b][i])
    return 1

def check_seq(b, a): # 스도쿠 사각형들이 모두 스도쿠 만족하는지
    # 카운트하며 나온 숫자가 또 나올 경우 return -1
    # [b, a] 좌표가 어느 사각형에 위치하는지 먼저 체크
    # 0 ~ 2, 3 ~ 5, 6 ~ 8 로 구분
    num_list = []
    if 0 <= b <= 2 and 0 <= a <= 2:
        for i in range(0, 3):
            for j in range(0, 3):
                if sudoku[i][j] == 0:
                    continue
                if num_list == []:
                    num_list.append(sudoku[i][j])
                else:
                    if sudoku[i][j] in num_list:
                        return -1
                    else:
                        num_list.append(sudoku[i][j])

    elif 0 <= b <= 2 and 3 <= a <= 5:
        for i in range(0, 3):
            for j in range(3, 6):
                if sudoku[i][j] == 0:
                    continue
                if num_list == []:
                    num_list.append(sudoku[i][j])
                else:
                    if sudoku[i][j] in num_list:
                        return -1
                    else:
                        num_list.append(sudoku[i][j])

    elif 0 <= b <= 2 and 6 <= a <= 8:
        for i in range(0, 3):
            for j in range(6, 9):
                if sudoku[i][j] == 0:
                    continue
                if num_list == []:
                    num_list.append(sudoku[i][j])
                else:
                    if sudoku[i][j] in num_list:
                        return -1
                    else:
                        num_list.append(sudoku[i][j])

    elif 3 <= b <= 5 and 0 <= a <= 2:
        for i in range(3, 6):
            for j in range(0, 3):
                if sudoku[i][j] == 0:
                    continue
                if num_list == []:
                    num_list.append(sudoku[i][j])
                else:
                    if sudoku[i][j] in num_list:
                        return -1
                    else:
                        num_list.append(sudoku[i][j])

    elif 3 <= b <= 5 and 3 <= a <= 5:
        for i in range(3, 6):
            for j in range(3, 6):
                if sudoku[i][j] == 0:
                    continue
                if num_list == []:
                    num_list.append(sudoku[i][j])
                else:
                    if sudoku[i][j] in num_list:
                        return -1
                    else:
                        num_list.append(sudoku[i][j])

    elif 3 <= b <= 5 and 6 <= a <= 8:
        for i in range(3, 6):
            for j in range(6, 9):
                if sudoku[i][j] == 0:
                    continue
                if num_list == []:
                    num_list.append(sudoku[i][j])
                else:
                    if sudoku[i][j] in num_list:
                        return -1
                    else:
                        num_list.append(sudoku[i][j])

    elif 6 <= b <= 8 and 0 <= a <= 2:
        for i in range(6, 9):
            for j in range(0, 3):
                if sudoku[i][j] == 0:
                    continue
                if num_list == []:
                    num_list.append(sudoku[i][j])
                else:
                    if sudoku[i][j] in num_list:
                        return -1
                    else:
                        num_list.append(sudoku[i][j])

    elif 6 <= b <= 8 and 3 <= a <= 5:
        for i in range(6, 9):
            for j in range(3, 6):
                if sudoku[i][j] == 0:
                    continue
                if num_list == []:
                    num_list.append(sudoku[i][j])
                else:
                    if sudoku[i][j] in num_list:
                        return -1
                    else:
                        num_list.append(sudoku[i][j])

    elif 6 <= b <= 8 and 6 <= a <= 8:
        for i in range(6, 9):
            for j in range(6, 9):
                if sudoku[i][j] == 0:
                    continue
                if num_list == []:
                    num_list.append(sudoku[i][j])
                else:
                    if sudoku[i][j] in num_list:
                        return -1
                    else:
                        num_list.append(sudoku[i][j])

    return 1


def find_sudoku_ans():
    # zero_list 순회하며 1 ~ 9 사이의 값 넣고 스도쿠 판단, 안되면 다른 수 넣기
    visited = [0] * len(zero_list)

    for i in range(len(zero_list)):
        for j in range(1, 10):
            b, a = zero_list[i]
            sudoku[b][a] = j
            if check_sero(a) and check_garo(b) and check_seq(b, a):
                visited[i] = True
                break
            else:
                sudoku[b][a] = 0
    
    return sudoku

sudoku = []
while True:
    try:
        sudoku.append(list(map(int, input())))
    except:
        break


# 0인 곳을 카운트하여 하나의 리스트로 만든다.
zero_list = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_list.append([i, j])

# 이제 이 zero_list에 값을 채우며 스도쿠를 만족하는지 못하는지를 판단하면 된다.

final_ans = find_sudoku_ans()
print(final_ans)