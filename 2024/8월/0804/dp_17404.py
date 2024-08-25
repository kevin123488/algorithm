import sys
sys.stdin = open('17404.txt')

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)] # 각 집을 빨, 초, 파로 칠하는 비용

# dp로 해결
# 집 개수만큼 칸을 만들자. 각 칸에는 3개의 칸을 만들어두자. 각각 빨, 초, 파 임
# dp[i - 1][0] -> i번째 집이 빨간색으로 칠해졌을 때 최소비용

# 시작값 고정하고 만들어보자
ans = 1000009
    
for first_color in range(3): # 0 -> 빨, 1 -> 초, 2 -> 파
    dp = [[1000009] * 3 for _ in range(n)]
    dp[0][first_color] = house[0][first_color]

    for i in range(1, n): # 집 순회
        dp[i][0] = min(dp[i - 1][1] + house[i][0], dp[i - 1][2] + house[i][0])
        dp[i][1] = min(dp[i - 1][0] + house[i][1], dp[i - 1][2] + house[i][1])
        dp[i][2] = min(dp[i - 1][0] + house[i][2], dp[i - 1][1] + house[i][2])
    
    for last_color in range(3):
        if last_color != first_color:
            ans = min(ans, dp[-1][last_color])

print(ans)