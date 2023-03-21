import sys
sys.stdin = open('input18428.txt')
from itertools import combinations
from copy import deepcopy

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def define_ans(copy_list):
    # 학생들을 선생님들의 감시 속에서 확실히 숨길 수 있다 -> YES 리턴
    for i in teacher:
        now = i
        for j in range(4):
            flag = 0  # 장애물 만나는 순간 1로 바뀜
            cnt = 1
            while True:
                ni = now[0] + di[j] * cnt
                nj = now[1] + dj[j] * cnt
                if 0 <= ni < N and 0 <= nj < N:
                    # 학생을 안만나거나, 학생을 만나기 전에 장애물을 만나면 됨
                    if copy_list[ni][nj] == 'O':
                        flag = 1
                    if flag == 0 and copy_list[ni][nj] == 'S':
                        return 'NO'
                    cnt += 1
                else:
                    break

    return 'YES'

def find_ans(copy_list):
    for i in blank_list_comb:
        copy_list[i[0][0]][i[0][1]] = 'O'
        copy_list[i[1][0]][i[1][1]] = 'O'
        copy_list[i[2][0]][i[2][1]] = 'O'
        if define_ans(copy_list) == 'YES':
            return 'YES'
        copy_list = deepcopy(arr)

    return 'NO'

# N*N 크기의 복도가 있다. 1*1 크기의 칸으로 나누어지고, 특정 위치에 선생님, 학생, 장애물이
# 위치해있다. 학생들은 선생님의 감시에 들키지 않는 것이 목표이다.
# 선생님들은 자기 위치에서 상하좌우 4가지 방향으로 감시를 진행한다.
# 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들을 볼 수 없다.
# 단 장애물이 없다면 상하좌우 방향에 있는 학생을 모두 확인할 수 있다.
# 선생님: T, 학생: S, 장애물: O
# 학생들은 복도의 빈 칸 중에서 장애물을 설치할 위치를 골라, 3개의 장애물을 설치해야 한다.
# 결과적으로 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 계산해야 한다.
# 가능하면 'YES', 불가능하면 'NO' 출력

N = int(sys.stdin.readline())
arr = []
blank_list = []
teacher = []
student_num = 0
for i in range(N):
    raw = list(sys.stdin.readline().split())
    for j in range(N):
        if raw[j] == 'X':
            blank_list.append([i, j])
        elif raw[j] == 'S':
            student_num += 1
        else:
            teacher.append([i, j])
    arr.append(raw)

blank_list_comb = list(combinations(blank_list, 3))
copy_list = deepcopy(arr)
print(find_ans(copy_list))