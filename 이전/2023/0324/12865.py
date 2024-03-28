import sys
sys.stdin = open('input12865.txt')

def knapsack(capacity, n):
    dp = [[0] * (capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if size[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(value[i-1] + dp[i-1][j-size[i-1]], dp[i-1][j])
    return dp[n][capacity]

N, K = map(int, input().split()) # N: 물건의 수, K: 배낭 용량 상한치
size = []
value = []

for i in range(N):
    s, v = map(int, input().split())
    size.append(s)
    value.append(v)

print(knapsack(K, N))
