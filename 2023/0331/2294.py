import sys
sys.stdin = open('input2294.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
# n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수는 최소가 되게 하려고 한다.
# 각각의 동전은 몇 개라도 사용할 수 있다.
# 사용한 동전의 구성이 같은데 순서만 다른 것은 같은 경우이다.
coin = [int(input()) for _ in range(n)]
coin.sort()
arr = []
for i in coin:
    if i in arr:
        pass
    else:
        arr.append(i)

# [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# [1, 1, 2, 3, 4, 1, 2, 3, 4, 5,  2,  3,  4,  5,  6,  3]
# [1, 1, 2, 3, 4, 1, 2, 3, 4, 5,  2,  3,  1,  2,  3,  3]
dp = [100001] * (k + 1)
dp[0] = 0
for i in arr:
    for j in range(i, k + 1):
        dp[j] = min(dp[j], dp[j-i] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])