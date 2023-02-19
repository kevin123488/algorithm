import sys
sys.stdin = open('11047input.txt')

def return_coin(coin, K):
    coin_num = K//coin
    last_money = K - (K//coin * coin)
    return coin_num, last_money

# 동전 N 종류
# 동전을 사용, 가치의 합을 K로 만들고자 함
# 필요한 동전 개수의 최솟값을 구해 보자

N, K = map(int, input().split())
arr = [] # 동전의 종류가 들어갈 리스트
for i in range(N):
    arr.append(int(input()))

# 특정 동전을 이용해 K값을 맞추려 할 때 필요한 동전 수와 남는 값을 반환하는 함수를 만들자
ans = 0
for i in range(N-1, -1, -1):
    semi_ans, K = return_coin(arr[i], K)
    ans += semi_ans

print(ans)