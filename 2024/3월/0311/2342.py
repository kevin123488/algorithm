import sys
sys.stdin = open('2342.txt')
import pprint

def power_cal(a, b): # a -> b로 이동할 때
    if a == 0:
        return 2
    elif a == b:
        return 1
    elif abs(a - b) == 2:
        return 4
    else:
        return 3


ddr = list(map(int, input().split()))
n = len(ddr)

# dp를 어떤 형태로 만들어야 할까? -> 오른발, 왼발, 누적 힘과 관련된 정보를 저장할 필요가 있다.
# 1차원 -> 왼발, 2차원 -> 오른발, 3차원 -> 몇번째

dp = [[[500000] * 5 for _ in range(5)] for _ in range(n)]

# 시작점: 0, 0, 0
# 첫 발 -> 1, 0, 합
#       -> 0, 1, 합
# 두번째 발 -> 1, 1, 합
#           -> 2, 0, 합
#           -> 1, 1, 합
#           -> 0, 2, 합

dp[0][0][0] = 0

for i in range(n - 1):
    next_board = ddr[i]
    for j in range(5):
        for k in range(5):
            dp[i + 1][j][next_board] = min(dp[i + 1][j][next_board], dp[i][j][k] + power_cal(k, next_board))
            dp[i + 1][next_board][k] = min(dp[i + 1][next_board][k], dp[i][j][k] + power_cal(j, next_board))

ans = 500000
for i in dp[n - 1]:
    ans = min(ans, min(i))
print(ans)