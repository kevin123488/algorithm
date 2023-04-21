import sys
sys.stdin = open('input11727.txt')
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001
dp[1] = 1 # 가로의 길이가 1인 사각형을 채우는 가짓수
dp[2] = 3
# 3일 경우 5
# 4일 경우 11
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n]%10007)