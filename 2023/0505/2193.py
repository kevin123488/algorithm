import sys
sys.stdin = open('input2193.txt')

n = int(input())
# 이친수 구하기
# 이친수는 0으로 시작하지 않음
# 이친수에서는 1이 두 번 연속으로 나타나지 않음(11을 부분 문자열로 갖지 않는다는 뜻)
# n이 주어졌을 떄, n자리 이친수의 개수를 구하여라

dp = [0] * (n + 1) # n번째 인덱스에 n자리의 이친수의 개수를 입력
fin_0 = [0] * (n + 1)
fin_1 = [0] * (n + 1)
dp[1] = 1
fin_0[1] = 0
fin_1[1] = 1
if n > 1:
    dp[2] = 1
    fin_0[2] = 1
    fin_1[2] = 0
if n > 2:
    dp[3] = 2
    fin_0[3] = 1
    fin_1[3] = 1

for i in range(1, n + 1):
    if i > 3:
        # 이전거에서 0으로 끝나는 이친수 * 2 + 1로 끝나는 이친수
        fin_0[i] = fin_0[i - 1] + fin_1[i - 1]
        fin_1[i] = fin_0[i - 1]
        dp[i] = fin_0[i - 1] * 2 + fin_1[i - 1]

print(dp[n])