import sys
sys.stdin = open('input9251.txt')
input = sys.stdin.readline

a = list(input().strip())
b = list(input().strip())
# a와 b의 공통 부분수열중 가장 긴 부분을 출력하는 문제
# ACAYKP와 CAPCAK의 LCS는 ACAK가 됨
# ACAKP가 아닌 이유 -> 두번째 문자열은 ACAKP 순으로 알파벳이 진행되지 않음. 그러므로 정답은 ACAK
# 간단히 말해 첫 문자열과 두번째 문자열에서 특정 부분을 삭제한 후 같아지는 부분의 길이가 최대가 되도록 하면 되는 것
dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(a)][len(b)])