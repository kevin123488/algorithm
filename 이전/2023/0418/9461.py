import sys
sys.stdin = open('input9461.txt')
input = sys.stdin.readline

t = int(input())
for i in range(t):
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    n = int(input())
    for j in range(6, n+1):
        if j > 5:
            dp[j] = dp[j-1] + dp[j-5]

    print(dp[n])