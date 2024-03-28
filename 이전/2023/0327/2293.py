import sys
sys.stdin = open('input2293.txt')

n, k = map(int, sys.stdin.readline().split())
arr = list(int(sys.stdin.readline()) for _ in range(n))
arr.sort()

# n가지 종류의 동전이 있다. 각 동전이 나타내는 가치는 다르다. 이 동전을 활용, 그 가치의 합이 k원이 되는 경우의 수는?
# 각 동전은 몇 개 씩이고 사용 가능하다.
# k가 10이고 동전이 1, 2, 5 이렇게 있다 치자
# 1을 만드는 가짓수 -> 1
# 2를 만드는 가짓수 -> 11, 2
# 5를 만드는 가짓수 -> 11111, 1211, 122, 5
# 10을 만드는 방법 ->
dp = [0] * (k+1)
dp[0] = 1

for i in arr:
    for j in range(i, k+1):
        dp[j] = dp[j] + dp[j-i]

print(dp[k])