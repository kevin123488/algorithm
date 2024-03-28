import sys
sys.stdin = open('input2630.txt')
input = sys.stdin.readline

def find_ans(s_i, s_j, n): # 0 0 4
    global cnt_w, cnt_b
    cnt = 0
    color = []
    flag = 0
    for i in range(s_i, s_i + n):
        if flag == 1:
            break
        for j in range(s_j, s_j + n):
            if cnt == 0:
                color.append(arr[i][j])
                cnt += 1
            else:
                if color[-1] != arr[i][j]: # 더 나눠야 하는 경우
                    find_ans(s_i, s_j, n//2)
                    find_ans(s_i + n//2, s_j, n//2)
                    find_ans(s_i, s_j + n//2, n//2)
                    find_ans(s_i + n//2, s_j + n//2, n//2)
                    flag = 1
                    break
    if flag == 0:
        if color[0] == 1:
            cnt_b += 1
        else:
            cnt_w += 1
    return

# 파란색 -> 1, 하얀색 -> 0
# 이 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려 한다.
n = int(input()) # 전체 종이의 크기는 8 * 8, n은 2**k의 형태
# 전체 종이가 모두 같은 색으로 칠해져 있지 않다 -> 가로와 세로 중간 부분을 잘라서 4등분
# 잘린 종이가 모두 단색(모두 하얀색으로 칠해져 있거나 파란색으로 칠해져 있을 경우)이 될 때까지 반복
# 잘린 아웃풋에 대해 흰 색종이와 파란색 색종이의 개수를 구해보자

arr = [list(map(int, input().split())) for _ in range(n)]
cnt_w = 0
cnt_b = 0
find_ans(0, 0, n)
print(cnt_w)
print(cnt_b)