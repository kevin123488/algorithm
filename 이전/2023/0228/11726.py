import sys
sys.stdin = open('11726input.txt')

n = int(input())
# 2*n 크기의 직사각형을 1*2, 2*1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하라
# dp 사용, 2*1 일때의 값을 ans_list의 1번째 값에, 2*2 일때의 값을 ans_list의 2번째 값에 저장

# ans_list = [0 for _ in range(n+1)] # 인덱스와 n값을 맞춰주기 위해
# for i in range(1, n+1):
#     if i == 1:
#         ans_list[i] = 1
#     elif i == 2:
#         ans_list[i] = 2
#     elif i == 3:
#         ans_list[i] = 3
#     # 1~10까지 예로 들어보면
#     # 1, 2, 3, 5, 8, 13, 21, 34, 55
#     else:
#         ans_list[i] = ans_list[i-1] + ans_list[i-2]
#
# print(ans_list[n]%10007)

ans_list = [0, 1, 2, 3, 0]
ans1 = 1
ans2 = 2
ans3 = 3
ans4 = 0
if n <= 3:
    print(ans_list[n])
else:
    for i in range(1, n-2):
        # ans_list[4] = ans_list[2] + ans_list[3]
        # if i == n:
        #     break
        # ans_list = ans_list[1:] + [0]
        ans4 = ans2 +  ans3
        ans2 = ans3
        ans3 = ans4

    print(ans4%10007)