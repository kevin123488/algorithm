import sys
sys.stdin = open('11052.txt')

n = int(input())
p = list(map(int, input().split()))

# 등급 8가지. 전설, 레드, 오렌지, 퍼플, 블루, 청록, 그린, 그레이
# 카드팩 종류 n가지, 1개 카드 포함팩, ... , n개 카드 포함팩
# 카드 개수가 적더라도 가격이 비싸면 높은 등급의 카드가 많이 있을것이라는 상상함. 그래서 돈을 최대한 많이 지불하여 카드 N개 구매하려 함
# 카드 i개 포함된 카드팩은 pi원
# P1 = 1, P2 = 5, P3 = 6, P4 = 7, n = 4일 때 지불 가능한 케이스는 1. 1 * 4, 2. 2 * 1 + 1 * 2, 3. 2 * 2, 4. 3 * 1 + 1 * 1, 5. 4 * 1.
# 위의 케이스들 중 가장 높은 값을 지불하는 케이스는 2번 2 * 2. 10원 지불.
# 카드팩의 가격이 주어졌을 때 n개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값은?

dp = [0] * (n + 1) # 0부터 n까지 리스트 만들자
p = [0] + p
dp[0] = 0
dp[1] = p[1]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if i + j <= n:
            dp[i + j] = max(p[i + j], dp[i] + dp[j], dp[i + j])

# i, j -> (1, 1), (1, 2), (1, 3), (1, 4), (2, 1)
print(dp[n])

# 6
# 1 5 6 1 1 1

# dp = [0, 0, 0, 0, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0]
# 