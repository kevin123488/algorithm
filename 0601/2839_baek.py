import sys
sys.stdin = open('2839_input.txt')

# 설탕공장에서 설탕 배달중인 상근
# Nkg를 배달해야 함
# 봉지는 3kg와 5kg봉지가 있음
# 봉지를 최소개수로 들고가려 함
N = int(input())
# 만약 딱 맞춰서 Nkg을 챙길 수 있다면, 해당하는 최소치를 보이고 (18kg일 경우, 5kg 3개, 3kg 1개)
# 딱 맞춰서 가져오는게 불가능하다면 -1을 출력
# 1. 딱 맞출 수 있는지 없는지 판별
# 2-1. 맞출 수 있다면? 5kg짜리가 가장 많이 사용되는 경우를 출력
# 2-2. 맞출 수 없다면? -1 출력

# 3x + 5y = N을 만족하는 x,y쌍을 찾자
ans_list = []
for i in range(N//3+2):
    for j in range(N//5+2):
        if 3*i + 5*j == N:
            ans_list.append(i+j)

if ans_list == []:
    print(-1)
else:
    print(min(ans_list))