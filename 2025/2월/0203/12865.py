import sys
sys.stdin = open('input_12865.txt')

n, k = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(n)] # 무게, 가치

# 냅색 문제
dp = [[0] * n for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(n):
        if things[j] + dp[i - 1][j] <= k:
            dp[i][j] = things[j] + dp[i - 1][j]