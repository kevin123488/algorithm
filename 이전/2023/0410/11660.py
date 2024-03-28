import sys
sys.stdin = open('input11660.txt')
input = sys.stdin.readline

# n*n의 표가 주어짐
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 0, 0에서 특정 지점까지의 합을 구해보자
# 1 3 6 10
# 3 8 15
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][1] = arr[0][0]
ans_i0 = arr[0][0]
ans_j0 = arr[0][0]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j > 1:
            ans_i0 += arr[i-1][j-1]
            dp[i][j] = ans_i0
        elif j == 0 and i > 0:
            ans_j0 += arr[i-1][j-1]
            dp[i][j] = ans_j0
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i-1][j-1] - dp[i-1][j-1]

for tc in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다.


    # print(dp[x2][y2] - dp[x1][y1] + arr[x1][y1])
    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1]) + dp[x1-1][y1-1])


# a         a+b            a+b+c
# a+d     a+b+d+e       a+b+c+d+e+f